import pandas as pd
import argparse
import re
from NLP.utils import handle_pickle, condition_id
from NLP.utils import list_of_columns_transcription
# setting up CLI


#TODO specify path to save pickle file

parser = argparse.ArgumentParser(description = "Transcription processing")
parser.add_argument("transcription_csv", help = "path to the csv file containing the transcriptions")
parser.add_argument("output_dic", help = "path to the output directory")
args = parser.parse_args()


df = pd.read_csv(args.transcription_csv)
df = df[list_of_columns_transcription]




def process_rated_transcription (input_path, output_dic):
    """
    Takes anonymized transcriptions, after they have been rated by annotators, and save them to a csv file
    along with their corresponding id, condition, mode and station.
    Args:
        input_path: path to csv file that contains the rated transcriptions.
        output_dic: path to save clean_transcription.csv file
    Returns:

    """
    dic_data ={
        'id':[],
        'rating':[],
        'condition':[],
        'mode':[],
        'station':[],
        'transcription':[]

    }
    condition_id_dictionary = {y:x for x,y in condition_id.items()}
    df = pd.read_csv(input_path, sep=';')


    regex_station = re.compile(r'[0-9]')
    column_id = re.compile(r'([0-9]{1,2})_([0-9]{1,2})')
    for index, row in df.iterrows():
        id_condition = column_id.search(row['id_transcription']).groups()
        dic_data['id'].append(int(id_condition[0]))
        dic_data['rating'].append([row['Rating']])
        condition_mode_station = condition_id_dictionary[id_condition[1]]
        station_num = regex_station.search(condition_mode_station)[0]
        if 'Blob' in condition_mode_station:
            dic_data['condition'].append('Blob')
        else:
            dic_data['condition'].append('Avatar')
        if 'Hybrid' in condition_mode_station:
            dic_data['mode'].append('Hybrid')
        else:
            dic_data['mode'].append('Firstperson')

        dic_data['station'].append(regex_station.search(condition_mode_station)[0])
        dic_data['transcription'].append(row['transcription'])


    df = pd.DataFrame.from_dict(dic_data)

    # Exports information to a csv file after having sorted out by id.
    df.to_csv(output_dic + '/clean_transcription_df_8.csv', index=False)



process_rated_transcription(args.transcription_csv,args.output_dic)



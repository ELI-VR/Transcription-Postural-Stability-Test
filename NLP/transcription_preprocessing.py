import pandas as pd
import argparse
import re
from NLP.utils import condition_id
from NLP.utils import list_of_columns_transcription
# setting up CLI




parser = argparse.ArgumentParser(description = "Transcription processing")
parser.add_argument("--transcription", help = "path to the csv file containing the transcriptions to be anonymized", default=None)
parser.add_argument("--num_csvs_chunks", help = "number of chunks", default=None)
parser.add_argument("--path_rated_transcription", help = "path to the csv file containing the anonymized transcriptions along with their ratings", default=None)
parser.add_argument("--output_dir", help = "path to the output directory")
args = parser.parse_args()


def generate_radomized_data (path_csv_transcription, output_dir,num_csvs_chunks):
    """
    This function deletes the column names and shuffles the data so that human judges are left totally clueless as to
    what condition or to whom a transcription belongs to. This has the sole purpose of avoiding any kind of bias when
    human judges classify a transcription as: -first person -third person -undefined. This function also chunks the transcriptions
    into several csv files.
    Args:
    path_csv_transcription: path to the csv file containing the transcriptions.
    num_csvs_chunks: each csv is chunked into smaller size files.
    path_save_csv_anonymized: path to a folder to save csv files containing the shuffled chunks ready to be rated by annotators.

    Returns:

    """
    df = pd.read_csv(path_csv_transcription)
    df = df[list_of_columns_transcription]

    dict_radom_data = {
        'id_transcription': [], #the first number corresponds to the participant's id and the second one after the _, is the condition id
        'transcription': []
    }
    for index, row in df.iterrows():
        for column_name in list_of_columns_transcription[1:-1]:
            cell_transcription = row[column_name]
            if type(cell_transcription) != float:
                dict_radom_data['id_transcription'].append(str(row['id']) +'_'+ condition_id[column_name])
                dict_radom_data['transcription'].append(cell_transcription)
    #this data frame does not contain the heading names
    df_no_headings = pd.DataFrame.from_dict(dict_radom_data)
    #suffle (rows) data. This makes it more difficult for human judges to figure out to what condition or participant a transcription belongs to.
    df_shuffled = df_no_headings.sample(frac=1).reset_index(drop=True)
    #add a new column to the dataframe so that judges can enter their rating
    df_shuffled['Rating'] = ""

    def split_save_csv(num_chunks, path_save_csv_anonymized):
        starting_index = 0
        chunk_size = int(df_shuffled.shape[0] / num_chunks)
        for i in range(num_chunks):
            df_name = 'df_' + str(i)+'.csv'

            if i==num_chunks-1:
                df_shuffled.iloc[starting_index:].to_csv(path_save_csv_anonymized + df_name, index=False)
            else:
                df_shuffled.iloc[starting_index:starting_index+chunk_size].to_csv(path_save_csv_anonymized + df_name, index=False)
            starting_index= starting_index+chunk_size

    #split and save to a csv file
    split_save_csv(num_csvs_chunks, output_dir)






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
    df.to_csv(output_dic + '/clean_transcription.csv', index=False)



if args.transcription != None:

    generate_radomized_data(args.transcription,args.output_dir, args.num_csvs_chunks)
elif args.path_anonymized_transcription != None:

    process_rated_transcription(args.path_rated_transcription,args.output_dir)




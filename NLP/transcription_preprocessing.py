import pandas as pd
import argparse
import re
from NLP.utils import handle_pickle, condition_id
from NLP.utils import list_of_columns_transcription
# setting up CLI


#TODO specify path to save pickle file

parser = argparse.ArgumentParser(description = "Text analysis")
parser.add_argument("transcription_csv", help = "path to the csv file containing the transcriptions")
parser.add_argument("output_dic", help = "path to the output directory")
args = parser.parse_args()


df = pd.read_csv(args.transcription_csv)
df = df[list_of_columns_transcription]
print('')



def process_rated_transcription (path, output_dic):
    """

    Args:
        path: path to csv file that contains the rated transcriptions.
        output_dic: path to save clean_transcription.csv file
    Returns:

    """
    dic_data ={
        'id':[],
        'rating':[],
        'condition':[],
        'mode':[],
        'transcription':[]

    }
    condition_id_dictionary = {y:x for x,y in condition_id.items()}
    df = pd.read_csv(path, sep=';')


    column_id = re.compile(r'([0-9]{2})_([0-9]{2})')
    for index, row in df.iterrows():
        id_condition = column_id.search(row['id_transcription']).groups()
        dic_data['id'].append(int(id_condition[0]))
        dic_data['rating'].append([row['Rating']])
        condition_mode_station = condition_id_dictionary[id_condition[1]]
        if 'Blob' in condition_mode_station:
            dic_data['condition'].append('Blob')
        else:
            dic_data['condition'].append('Avatar')
        if 'Hybrid' in condition_mode_station:
            dic_data['mode'].append('Hybrid')
        else:
            dic_data['mode'].append('Firstperson')

        dic_data['transcription'].append(row['trascription'])

        print('')
    df = pd.DataFrame.from_dict(dic_data).sort_values(by=['id'])
    # Exports information to a csv file after having sorted out by id.
    df.to_csv(output_dic + '/clean_transcription.csv', index=False)




process_rated_transcription('/home/yesid/Documents/Master_semester3/VR/data/Linus_transcription/rated_transcription/df_0 processed.csv')






def create_condition_txt(column):
    #TODO this can be implemented using map()
    text=''
    for cell in column:
        if type(cell) != float:
            #TODO delete /n
            text = f'{text}  \n {str(cell)}'
            #text= text + '\n' + str(cell)
    return text

def create_text (df_transcription):
    """
    Creates a whole text from the transcriptions belonging to each condition.
    Args:
        df_transcription: Data frame containing the transcriptions

    Returns:

    """

    #this regex returns the name of the column
    column_regex = re.compile(r'([A-Za-z]*)\s?\_?([0-9]$)')
    #list of the columns
    columns = df_transcription.columns
    columns=columns[1:-1]
    #column_name= lambda count: column_regex.search(columns[count]).groups()[0]
    text={}
    for column in columns:
        text[column]=[create_condition_txt(df_transcription[column])]

    handle_pickle(args.output_dic,text)
#create_text(df)


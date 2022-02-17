import pickle
import pandas as pd
import  numpy as np
import pathlib

list_of_columns_transcription= ['id','BlobFirstperson_0', 'BlobFirstperson_1', 'BlobFirstperson_2',
       'BlobFirstperson_4', 'BlobHybrid_0', 'BlobHybrid_1', 'BlobHybrid_2',
       'BlobHybrid_4', 'AvatarFirstperson_1', 'AvatarFirstperson_0',
       'BlobHybrid_3', 'BlobFirstperson_3', 'AvatarHybrid_1', 'AvatarHybrid_0',
       'AvatarHybrid_4', 'AvatarHybrid_3', 'AvatarHybrid_2',
       'AvatarFirstperson_4', 'AvatarFirstperson_3', 'AvatarFirstperson_2']

condition_id ={
    'BlobFirstperson_0':'1',
    'BlobFirstperson_1': '2',
    'BlobFirstperson_2': '3',
    'BlobFirstperson_3': '4',
    'BlobFirstperson_4': '5',
    'BlobHybrid_0': '6',
    'BlobHybrid_1': '7',
    'BlobHybrid_2': '8',
    'BlobHybrid_3': '9',
    'BlobHybrid_4': '10',
    'AvatarHybrid_0':'11',
    'AvatarHybrid_1':'12',
    'AvatarHybrid_2':'13',
    'AvatarHybrid_3':'14',
    'AvatarHybrid_4':'15',
    'AvatarFirstperson_0':'16' ,
    'AvatarFirstperson_1':'17',
    'AvatarFirstperson_2':'18',
    'AvatarFirstperson_3':'19',
    'AvatarFirstperson_4':'20'

}

def generate_radomized_data (path_csv_transcription, num_csvs_chunks):
    """
    This function deletes the column names and shuffles the data so that human judges are left totally clueless as to what condition or to whom a
    transcription belongs to. This has the sole purpose of avoiding any kind of bias when human judges classify a transcription as:
    -first person
    -third person
    -undefined
    Args:
        path_csv_transcription: path to the csv file containing the transcriptions.
        num_csvs_chunks: each csv is chunked into smaller size files.

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
    #this data frame does not contain the name of the headings
    df_no_headings = pd.DataFrame.from_dict(dict_radom_data)
    #suffle (rows) data. This makes it more difficult for human judges to figure out to what condition or participant a transcription belongs to.
    df_shuffled = df_no_headings.sample(frac=1).reset_index(drop=True)
    #add a new column to the dataframe so that judges can enter their rating
    df_shuffled['Rating'] = ""

    def split_save_csv(num_chunks,path_save_csv):
        starting_index = 0
        chunk_size = int(df_shuffled.shape[0] / num_chunks)
        for i in range(num_chunks):
            df_name = 'df_' + str(i)+'.csv'

            if i==num_chunks-1:
                df_shuffled.iloc[starting_index:].to_csv(path_save_csv+df_name,index=False)
            else:
                df_shuffled.iloc[starting_index:starting_index+chunk_size].to_csv(path_save_csv+df_name, index=False)
            #print(f'starting: {starting_index} end: {starting_index+chunk_size}')
            starting_index= starting_index+chunk_size
            #print(starting_index)
            #l = pd.read_csv(path_save_csv+df_name)
            #print(f'this is the size of the datafram: {l.shape[0]}')


    #split and save to a csv file
    split_save_csv(num_csvs_chunks,'/home/yesid/Documents/Master_semester3/VR/data/Linus_transcription/second_round_transcription/randomized_files/')

    print('')


generate_radomized_data('/home/yesid/Downloads/transcription_long_files.csv',2)



def merge_csv ():
    """
    Concatenates all csv files after human judges rated the transcriptions.
    IMPORTANT! store all csv files in a separate folder. 
    Returns:

    """
    csv_files = list(pathlib.Path('/home/yesid/Documents/Master_semester3/VR/postural_stability_analysis/data/csvs').glob('*.csv'))
    list_data_frames = []
    for path in csv_files:
        list_data_frames.append(pd.read_csv(path))
    whole_data = pd.concat(list_data_frames, axis=0)
    whole_data= whole_data.set_index('id').sort_index(ascending=True)
    whole_data.reset_index(inplace=True)
    whole_data.to_csv('/home/yesid/Documents/Master_semester3/VR/postural_stability_analysis/data'+'/all_velocities.csv', index=False)
    print('')

#merge_csv()



def handle_pickle(path, data=None, open_file=False):
    """
    saves and opens pickle file
    Args:
        path: path to save/open pickle file. When passing the path do not include the name of the pickle file.
        data: Object to be saved to pickle file
        open_file: if true, opens a pickle file

    Returns:

    """
    path= path + '/text_per_condition.pickle'

    if open_file:

        # Load data
        with open(path, 'rb') as handle:
            unserialized_data = pickle.load(handle)


        return unserialized_data
    else:
        # Save data
        with open(path, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)




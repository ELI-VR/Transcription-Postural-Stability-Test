import pickle
import pandas as pd


df_transcription = pd.read_csv('/home/yesid/Documents/Master_semester3/VR/data/Linus_transcription/transcription.csv')

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

def generate_radomized_data (path_csv_transcription):
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
        print('')



generate_radomized_data('/home/yesid/Documents/Master_semester3/VR/data/Linus_transcription/transcription.csv')



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




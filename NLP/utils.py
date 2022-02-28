import pickle
import pandas as pd
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


def merge_csv (input_dir_csv, output_concat):
    """
    Concatenates all csv files in a folder.
    IMPORTANT! store all csv files in a separate folder.
    Args:
        input_dir_csv: path to the directory containing a set of cvs files.
        output_concat: path to store resulting csv file. Include the csv file name e.g. /concatenated_csvs.csv
    Returns:

    """
    csv_files = list(pathlib.Path(input_dir_csv).glob('*.csv'))
    list_data_frames = []
    for path in csv_files:
        list_data_frames.append(pd.read_csv(path))
    whole_data = pd.concat(list_data_frames, axis=0)
    whole_data= whole_data.set_index('id').sort_index(ascending=True)
    whole_data.reset_index(inplace=True)
    whole_data.to_csv(output_concat, index=False)




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




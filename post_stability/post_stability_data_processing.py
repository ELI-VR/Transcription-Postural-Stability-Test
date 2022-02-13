from pathlib import Path
import os
import argparse
import pandas as pd
import re
import json


# setting up CLI


#TODO add this to corresponding sh file
#TODO use genearators to read data fron csv files

parser = argparse.ArgumentParser(description = "Preprocessing")
parser.add_argument("input_dic", help = "path to the input directory") #this directory will also contain the csv file with paths to the json files
parser.add_argument("output_dic", help = "path to the output directory, where csv velocities is stored")
args = parser.parse_args()

#TODO this function is repeaed from audio_preprocessing. integrate in a dingle moudule and then export
def extract_files(path):

    # path to all .json files
    paths = list(Path(path).rglob('*.json'))
    files= [x for x in paths if x.is_file()]
    return files

#extract_files('/home/yesid/Documents/Master_semester3/VR/postural_stability_analysis/data')
def process_json_files(files):

    # regular expression to extract ids
    id_regex = re.compile(r'^[0-9]{1,5}')
    #regular expression to extract the name of the condition
    #condition_regex = re.compile(r'([A-Za-z]*)\s?\_?([0-9]*$)')
    condition_regex = re.compile(r'[^_0-9]*[a-z]')
    # stores ids and paths to clean audio files
    data_dic = {
        'id': [],
        'path_to_json': [],
        'type': [] #there are two possibilities: 1) live 2)data_overview

    }

    for item in files:
        # file names
        file_name = os.path.basename(item)
        id_num = id_regex.search(file_name)

        # Load some audio
        data_dic['id'].append(id_num.group())
        data_dic['path_to_json'].append(item)
        #condition_name = condition_regex.search(item.stem).groups()
        condition_name = condition_regex.search(item.stem)
        if 'lv' in file_name:

            data_dic['type'].append(condition_name[0])
        else:

            data_dic['type'].append('data_overview') #condition's name


    df = pd.DataFrame.from_dict(data_dic).sort_values(by=['id'])
    # Exports information to a csv file after having sorted out by id.
    df.to_csv(args.output_dic + '/json_files.csv', index=False)
    # save not processed recording to a csv file
    return  df



def get_time_stamps (df):

    dict_data ={
        'id':[],
        'path':[],
        'condition':[],
        'station':[],
        'time_frame_begin':[],
        'time_frame_end': []
    }
    #filter by .json files cotaning information about all stations of a condition.
    df_data_overview = df[df['type'] == 'data_overview']
    for index, row in df_data_overview.iterrows():

        #this file contains information about all stations for one condition
        f = open(row['path_to_json'])
        data = json.load(f)
        condition = data['Condition']
        participant_id = data['participantID']
        #df_by_id = df[df['id'] == row[participant_id]]
        for num, station in enumerate (data['_stationDataFrames']):
            stationID = station['stationID']
            stationIndex= station['stationIndex']
            #fetch json file

            #path to json file containing time stamps for one station, say station 1 condition BlobFirstperson
            #TODO make sure that this path actually exists.
            file_stamp_time = '/'+participant_id+'_'+condition+'_S'+str(stationID)+'_I'+str(stationIndex)+'_lv.json'
            path_json = Path(args.input_dic + file_stamp_time)
            #check if the file exists
            if df[df['path_to_json']==path_json].empty:
                print(f"This file {file_stamp_time} could not be found, hence could not extract time stamps. For information check out {row['path_to_json']}")
            else:
                dict_data['id'].append(participant_id)
                dict_data['path'].append(path_json)
                dict_data['condition'].append(condition)
                dict_data['station'].append(stationID)
                dict_data['time_frame_begin'].append(station['PosturalStabilityTimeFrameBegin'])
                dict_data['time_frame_end'].append(station['PosturalStabilityTimeFrameEnd'])
        f.close()
    #save dictionary to df and the to csv
    df_timestamps = pd.DataFrame.from_dict(dict_data).sort_values(by=['id'])
    # Exports information to a csv file after having sorted out by id.
    df_timestamps.to_csv(args.output_dic + '/timestamps.csv', index=False)

get_time_stamps(process_json_files(extract_files(args.input_dic)))



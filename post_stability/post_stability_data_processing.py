from pathlib import Path
import os
import argparse
import pandas as pd
import re
import json
from scipy.spatial import distance

# setting up CLI


#TODO add this to corresponding sh file
#TODO use genearators to read data fron csv files



#TODO this function is repeaed from audio_preprocessing. integrate in a dingle moudule and then export
def extract_files(path):

    # path to all .json files
    paths = list(Path(path).rglob('*.json'))
    files= [x for x in paths if x.is_file()]
    return files

def process_json_files(files, output_dic):

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
    #todo uncomment this line
    #df.to_csv(output_dic + '/json_files.csv', index=False)
    # save not processed recording to a csv file
    return  df



def get_time_stamps (df,input_dic,output_dic):

    print(f'this is the number of files to be processed: {df.shape[0]}')
    dict_data ={
        'id':[],
        'path':[],
        'condition':[],
        'mode':[],
        'condition_mode':[],
        'station':[],
        'time_frame_begin':[],
        'time_frame_end': [],
        'motion_sickness_score':[],
        'name_of_audio_data':[],
        'motionsickness_score_rating_begin':[],
        'motionsickness_score_rating_accepted_timeStamp':[]
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
            path_json = Path(input_dic + file_stamp_time)
            #check if the file exists
            if df[df['path_to_json']==path_json].empty:
                print(f"This file {file_stamp_time} could not be found, hence could not extract time stamps. For information check out {row['path_to_json']}")
            else:
                dict_data['id'].append(participant_id)
                dict_data['path'].append(path_json)
                if 'Blob' in condition:

                    dict_data['condition'].append('Blob')
                else:
                    dict_data['condition'].append('Avatar')
                if 'Hybrid' in condition:
                    dict_data['mode'].append('hybrid')
                else:
                    dict_data['mode'].append('Firstperson')
                dict_data['condition_mode'].append(condition)
                dict_data['station'].append(stationID)
                dict_data['time_frame_begin'].append(station['PosturalStabilityTimeFrameBegin'])
                dict_data['time_frame_end'].append(station['PosturalStabilityTimeFrameEnd'])
                dict_data['motion_sickness_score'].append((station['MotionsicknessScore']))
                dict_data['name_of_audio_data'].append(station['NameOfAudioData'])
                dict_data['motionsickness_score_rating_begin'].append(station['MotionsicknessScoreRatingBegin'])
                dict_data['motionsickness_score_rating_accepted_timeStamp'].append(station['MotionsicknessScoreRatingAcceptedTimeStamp'])

        f.close()
    #save dictionary to df and the to csv
    df_timestamps = pd.DataFrame.from_dict(dict_data).sort_values(by=['id'])
    # Exports information to a csv file after having sorted out by id.

    df_timestamps.to_csv(output_dic + '/timestamps.csv', index=False)
    return df_timestamps

def compute_velocities(df, output_dic):

    print(f'this is the number of files to be processed (VELOCITY0: {df.shape[0]})')
    """

    Args:
        df: data frame with the time stamps

    Returns:

    """
    #todo add these as  columns to the data frame that contains the time stamp being/end

    #id_velocities= []
    average_velocity_list= []

    count =0
    for index, row in df.iterrows():
        count+=1
        #load json with the time stamps
        f = open(row['path'])
        #type list
        data = json.load(f)
        # using PosturalStabilityTimeFrameBegin and PosturalStabilityTimeEnd, select the time stamps within this interval
        #time_s contains ALL timestamps, that's why we need to filter out the ones within the interval PosturalStabilityTimeFrameBegin and PosturalStabilityTimeEnd
        time_s =[]
        for i in data:
            time_s.append(i['TimeStamp'])
        #filter timestamps between PosturalStabilityTimeFrameBegin and PosturalStabilityTimeFrameEnd
        filtered = [*filter(lambda t: t > row['time_frame_begin'] and t < row['time_frame_end'] , time_s)]
        #indexes for slicing list
        begin = time_s.index(filtered[0]) #in time_s (that contains all timestamps) looks for the indexes
        end = time_s.index(filtered[-1])
        #slice list
        data_slice = data[begin:end+1] # double check if this is inclusive
        #split data_slice into intervals
        starting =0
        #store the velocity per participant given a single station, e.g. velocities for paticipant id 001, condition: BlobFirstPerson station 0 live data
        list_velocity_participant =[]
        for num_slice in range(int(len(data_slice)/10)):
            interval = data_slice[starting:starting+10]
            starting= starting+10
            #todo double check that all vectors have ten dimensions.
            #compute time
            time= interval[-1]['TimeStamp'] - interval[0]['TimeStamp']
            #compute
            x_1,y_1,z_1 = interval[0]['HMDPositionGlobal'].items() #returns a tupple, the coordinate is in the [1] position
            x_2, y_2, z_2 = interval[-1]['HMDPositionGlobal'].items()
            distance_interval = distance.euclidean((x_1[1],y_1[1],z_1[1]),(x_2[1],y_2[1],z_2[1]))
            velocity = distance_interval/time
            list_velocity_participant.append(velocity) #here finishes the processing of a single lv file.

        #id_velocities.append(row['id'])
        average_velocity = sum(list_velocity_participant)/len(list_velocity_participant)
        average_velocity_list.append(average_velocity)
        f.close()
        if count % 30 ==0:
            print(f'lv.json files processed so far: {count} of {df.shape[0]}')
    #add dictionary to the data frame that contains the time stamps
    #df['id_velocities']=id_velocities
    df['average_velocity']= average_velocity_list
    #export results as csv
    df.to_csv(output_dic + '/velocities.csv', index=False)
    return df

# df = pd.read_csv('/home/yesid/Documents/Master_semester3/VR/postural_stability_analysis/data/timestamps.csv')
# compute_velocities(df,'/home/yesid/Documents/Master_semester3/VR/postural_stability_analysis/data')
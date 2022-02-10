from pathlib import Path
import os
import librosa
import soundfile as sf
import argparse
import pandas as pd
import re
import numpy as np


# setting up CLI



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
    condition_regex = re.compile(r'([A-Za-z]*)\s?\_?([0-9]*$)')

    # stores ids and paths to clean audio files
    data_dic = {
        'id': [],
        'path_to_json': [],
        'type': [] #there are two possibilities: 1) live 2)condition name

    }

    for item in files:
        # file names
        file_name = os.path.basename(item)
        id_num = id_regex.search(file_name)

        # Load some audio
        data_dic['id'].append(id_num.group())
        data_dic['path_to_json'].append(item)
        if 'lv' in file_name:
            data_dic['type'].append('live')
        else:
            condition_name = condition_regex.search(item.stem).groups()
            data_dic['type'].append(condition_name[0]) #condition's name

    df = pd.DataFrame.from_dict(data_dic).sort_values(by=['id'])
    # Exports information to a csv file after having sorted out by id.
    df.to_csv(args.output_dic + '/json_files.csv', index=False)
    # save not processed recording to a csv file



process_json_files(extract_files(args.input_dic))


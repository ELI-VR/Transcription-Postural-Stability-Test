from pathlib import Path
import os
import librosa
import soundfile as sf
import argparse
import pandas as pd
import re
import matplotlib.pyplot as plt
from post_stability.post_stability_data_processing import get_time_stamps,process_json_files,extract_files
from post_stability.post_stability_data_processing import compute_velocities



parser = argparse.ArgumentParser(description = "Preprocessing")
parser.add_argument("input_dic", help = "path to the input directory") #this directory will also contain the csv file with paths to the json files
parser.add_argument("output_dic", help = "path to the output directory, where csv velocities is stored")
args = parser.parse_args()


#df =process_json_files(extract_files(args.input_dic), args.output_dic)

def check_number_files (df):
    ids = list(pd.unique(df['id']))
    for i in ids:
        num_files = df[df['id']== i].shape[0]

        if num_files != 10:

            print(f"Participant id: {i}  has {num_files}  .json files")



df = pd.read_csv('/home/yesid/Documents/Master_semester3/VR/postural_stability_analysis/data/all_velocities.csv')
check_number_files(df)

#df_timestamps= get_time_stamps(df, args.input_dic, args.output_dic)

#compute_velocities(df_timestamps, args.output_dic)
df_timestamps= pd.read_csv('/home/yesid/Documents/Master_semester3/VR/postural_stability_analysis/data/75_2/timestamps.csv')
compute_velocities(df_timestamps, args.output_dic)
print('hi')






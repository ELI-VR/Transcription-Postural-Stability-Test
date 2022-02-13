from pathlib import Path
import os
import librosa
import soundfile as sf
import argparse
import pandas as pd
import re
#todo import all of these in one line
from post_stability.post_stability_data_processing import get_time_stamps
from post_stability.post_stability_data_processing import process_json_files
from post_stability.post_stability_data_processing import extract_files
from post_stability.post_stability_data_processing import compute_velocities



parser = argparse.ArgumentParser(description = "Preprocessing")
parser.add_argument("input_dic", help = "path to the input directory") #this directory will also contain the csv file with paths to the json files
parser.add_argument("output_dic", help = "path to the output directory, where csv velocities is stored")
args = parser.parse_args()

df =process_json_files(extract_files(args.input_dic), args.output_dic)
df_timestamps= get_time_stamps(df, args.input_dic, args.output_dic)

compute_velocities(df_timestamps)

print('hi')




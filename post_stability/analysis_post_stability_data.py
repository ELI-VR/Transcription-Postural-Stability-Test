from pathlib import Path
import os
import librosa
import soundfile as sf
import argparse
import pandas as pd
import re




parser = argparse.ArgumentParser(description = "Preprocessing")
parser.add_argument("json_files", help = "path to json_files.csv") #directory that contains csv with .json files
parser.add_argument("output_dic", help = "path to the output directory where files resulting from the analysis will be saved")
args = parser.parse_args()

df = pd.read_csv(args.json_files)
df_data_overview = df[df['type']=='data_overview']

#l = pd.read_json('/home/yesid/Downloads/Telegram Desktop/001_BlobFirstperson_03124.json')
print()



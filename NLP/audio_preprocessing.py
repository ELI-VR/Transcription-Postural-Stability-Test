from pathlib import Path
import os
import librosa
import soundfile as sf
import argparse
import pandas as pd
import re

# setting up CLI

parser = argparse.ArgumentParser(description = "Preprocessing")
parser.add_argument("input_dic", help = "path to the input directory")
parser.add_argument("output_dic", help = "path to the output directory, where csv and clean audio files are stored")
args = parser.parse_args()


def extract_files(path):

    # path to all .wav files
    paths = list(Path(path).rglob('*.wav'))
    files= [x for x in paths if x.is_file()]
    return files

def shorten_audio(files):
    # code adapted from https://librosa.org/doc/main/generated/librosa.load.html
    """
    Trims silence parts of the audio file.
    Parameters:
      files (str): Path to the raw audio files.
    """
    # store audio files that are not processed due to wrong naming conventions.
    not_processed = []
    # regular expression to extract ids
    id_regex = re.compile(r'^[0-9]{1,5}')
    #stores ids and paths to clean audio files
    data_dic ={
        'id':[],
        'path_clean_audio':[],
        'length':[]
    }

    for count, item in enumerate(files):
        # file names
        file_name = os.path.basename(item)
        id_num = id_regex.search(file_name)
        if id_num is not None:

            # Load some audio
            y, sr = librosa.load(item)
            # Trim the beginning and ending silence
            yt, index = librosa.effects.trim(y)
            # save trimmed audio file.
            path_trimmed= args.output_dic + '/' + file_name
            sf.write(path_trimmed, yt, sr)
            data_dic['id'].append(id_num.group())
            data_dic['path_clean_audio'].append(path_trimmed)
            data_dic['length'].append(librosa.get_duration(yt))
        else:
            not_processed.append(item)

    df = pd.DataFrame.from_dict(data_dic).sort_values(by =['id'])
    #Exports information to a csv file after having sorted out by id.
    df.to_csv(args.output_dic + '/clean_audio.csv', index=False)
    #save not processed recording to a csv file
    df_not_processed =pd.DataFrame(not_processed,columns=['path_not_processed'])
    df_not_processed.to_csv(args.output_dic + '/audio_not_processed.csv', index=False)




shorten_audio(extract_files(args.input_dic))




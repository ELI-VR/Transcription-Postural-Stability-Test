import torch
import librosa
from transformers import Wav2Vec2ForCTC,Wav2Vec2Processor
import re
import argparse
import pandas as pd
from pathlib import Path
import time


# setting up CLI
time.sleep(5)
parser = argparse.ArgumentParser(description = "Transcription")
parser.add_argument("input_csv", help = "path to the csv containing clean audio files")
parser.add_argument("output_csv", help = "path to save the the csv with transcription")
parser.add_argument("-l", "--language", help="Indicate the language", default=None)


print("hello1")
args = parser.parse_args()

df = pd.read_csv(args.input_csv)


"""
For the transcription of both English and German audio text, the following pretrained models were used:
https://huggingface.co/facebook/wav2vec2-large-robust-ft-libri-960h
https://huggingface.co/marcel/wav2vec2-large-xlsr-53-german
The code provided by the sources above was adapted according to the needs of this project. 
"""

class TranscriptionModel():
    def __init__(self,language):
        self.language = language
        if self.language == 'English':
            self.model_name = "facebook/wav2vec2-large-robust-ft-libri-960h"
        else:
            self.model_name = "marcel/wav2vec2-large-xlsr-53-german"

        self.model = Wav2Vec2ForCTC.from_pretrained(self.model_name)
        self.tokenizer = Wav2Vec2Processor.from_pretrained(self.model_name)

    def transcribe(self, file_name):
        """
        Transcribes audio to text
        :param file_name: Path to a single audio file.
        :return: String containing the transcription.
        """
        input_audio, sampling_rate = librosa.load(file_name, sr=16000)
        input_values = self.tokenizer(input_audio, return_tensors="pt", padding="longest",
                                      sampling_rate=16_000).input_values
        logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.tokenizer.batch_decode(predicted_ids)[0]
        print(transcription)
        return transcription


class Transcription (TranscriptionModel):

    def __init__(self,language):
        self.df_transcription = pd.DataFrame(
                columns=['id','Hybrid_0', 'Hybrid_1', 'Hybrid_2', 'Hybrid_3', 'Hybrid_4', 'FirstPerson_0',
                         'FirstPerson_1', 'FirstPerson_2', 'FirstPerson_3', 'FirstPerson_4',
                         'Blob_0', 'Blob_1', 'Blob_2', 'Blob_3', 'Blob_4',
                         'Bodiless_0', 'Bodiless_1', 'Bodiless_2', 'Bodiless_3', 'Bodiless_4'])
        #This dictionary contains all transcriptions belonging to a single participant.
        self.new_entry = {}
        self.column_regex = re.compile(r'([A-Za-z]*)\s?\_?([0-9]$)')
        self.flag_change= True
        self.participant_id =0
        self.transcription =''
        super().__init__(language)
    def save_data(self,row,save_dictionary=False, save_dataframe=False):
        if save_dictionary:
            try:
                # get the column name
                column_name = self.column_regex.search(Path(row['path_clean_audio']).stem).groups()
                # save transcription to dictionary
                self.new_entry[column_name[0] + '_' + column_name[1]] = [self.transcription]
            except Exception as e:
                print('there has been an error:',e.__class__)
                print(f'This file was not transcribed: {row["path_clean_audio"]}')

        if save_dataframe:
            # save transcriptions to a dictionary
            self.new_entry['id'] = self.participant_id
            new_entry_df = pd.DataFrame.from_dict(self.new_entry)
            # append transcription to the dataframe to be exported as csv
            self.df_transcription = self.df_transcription.append(new_entry_df)
            # clean dictionary
            self.new_entry = {}

    def __call__(self,df, output_csv):
        """

        Args:
            df: Dataframe contains path to the clean audio files
            output_csv: path to save the csv with transcription


        """

        for index, row in df.iterrows():

            #Delays execution of the next transcription, this gives sometime to computer to empty memory
            #waiting time in seconds
            time.sleep(10)

            if row['duration_after_trim'] > 50:
                continue

            if self.flag_change:
                self.participant_id = row['id']
                self.flag_change = False
            if self.participant_id == row['id']:
                #do transcription for that participant
                self.transcription =self.transcribe(row['path_clean_audio'])
                self.save_data(row,save_dictionary=True)

            else:
                self.save_data(row, save_dataframe=True)
                self.participant_id = row['id']
                #do trancription
                self.transcription = self.transcribe(row['path_clean_audio'])
                self.save_data(row, save_dictionary=True)

        #if the new entry_entry dictionary is not empty save the last data point.
        if bool(self.new_entry):
            self.save_data(row, save_dataframe=True)
        #save transcription as a csv file
        self.df_transcription.to_csv(output_csv + '/transcription.csv', index=False)


print(f'this is the language of transcription: {args.language}')
audio_to_text =Transcription(args.language)
audio_to_text(df, args.output_csv)


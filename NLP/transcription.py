import torch
import librosa
from transformers import Wav2Vec2ForCTC,Wav2Vec2Processor
import re
import argparse
import pandas as pd
from pathlib import Path
import time
from pydub import AudioSegment


# setting up CLI

parser = argparse.ArgumentParser(description = "Transcription")
parser.add_argument("input_csv", help = "path to the csv containing clean audio files")
parser.add_argument("output_csv", help = "path to save the the csv with transcription")
parser.add_argument("output_chunks", help = "path to the folder to store chunks per long audio file") #These files can, if needed, be checked by human judges
parser.add_argument("-l", "--language", help="Indicate the language", default=None)
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
        return transcription


class Transcription (TranscriptionModel):

    def __init__(self,language):
        #TODO delete these column names, as the column name is obtained from the path_clean_audio row from the clean_audio.csv,
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

    def process_long_files(self, row, output_chunks,max_length):
        file_name = self.column_regex.search(Path(row['path_clean_audio']).stem).groups
        long_audio = AudioSegment.from_wav(row['path_clean_audio'])
        list_trasncriptions =[]
        chunks = int(long_audio.duration_seconds / max_length)
        starting_time =0
        for i in range (chunks):
            audio_chunks = long_audio[starting_time: starting_time + max_length*1000]
            #export chunk
            path =output_chunks+'/'+ str(row['id'])+'_'+file_name[0]+'_'+file_name[1]+'_chunk_' +str(i)+'.wav'
            audio_chunks.export(path, format="wav")
            # do transcription
            list_trasncriptions.append(self.transcribe(path))

            starting_time = starting_time + max_length*1000
        if long_audio.duration_seconds % max_length > 0:
            audio_chunks = long_audio[starting_time:]
            path = output_chunks + '/' + str(row['id']) + '_' + file_name[0]+'_'+file_name[1] + '_chunk_' + str(i+1) + '.wav'
            audio_chunks.export(path, format="wav")
            #do transcription
            self.transcribe(path)
            list_trasncriptions.append(self.transcribe(path))
        #join all individual transcriptions into a single text.
        self.transcription = ' '.join(list_trasncriptions)


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

    def __call__(self,df, output_csv,output_chunks, max_length =50):
        """

        Args:
            df: Dataframe contains path to the clean audio files
            output_csv: path to save the csv with transcription
            output_chunks: path to save audio files chunks


        """

        for index, row in df.iterrows():

            #Delays execution of the next transcription, this gives sometime to the computer to empty memory
            #waiting time in seconds
            time.sleep(10)

            if self.flag_change:
                self.participant_id = row['id']
                self.flag_change = False
            if self.participant_id == row['id']:

                if row['duration_after_trim'] > max_length:
                    #do transcription for long files
                    self.process_long_files(row, output_chunks,max_length)  #TEST HERE


                else:

                    #do transcription for that participant
                    self.transcription =self.transcribe(row['path_clean_audio'])
                # save transcription
                self.save_data(row,save_dictionary=True)

            else:
                self.save_data(row, save_dataframe=True)
                self.participant_id = row['id']
                #do trancription
                if row['duration_after_trim'] > max_length:
                    self.process_long_files(row, output_chunks, max_length)
                else:

                    self.transcription = self.transcribe(row['path_clean_audio'])
                self.save_data(row, save_dictionary=True)

        #if the new entry_entry dictionary is not empty save the last data point.
        if bool(self.new_entry):
            self.save_data(row, save_dataframe=True)
        #save transcription as a csv file
        self.df_transcription.to_csv(output_csv + '/transcription.csv', index=False)


print(f'this is the language of transcription: {args.language}')
audio_to_text =Transcription(args.language)
audio_to_text(df, args.output_csv, args.output_chunks)


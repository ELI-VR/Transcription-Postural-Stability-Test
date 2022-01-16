#!/bin/bash

#create directory if not yet existing
#mkdir -p data/clean_audio_data/
#mkdir -p data/transcription/
#mkdir -p data/visualizations
#first argument is the path to the raw audio data, if not not specified, the following path is assumed: data/raw_audio_data

if [ $1 ];
  then
    raw_path=$1

  else
    raw_path="data/raw_audio_data"
fi


echo "  Preprocessing"

python -m NLP.audio_preprocessing ${raw_path} /home/yesid/Desktop/mock_data/clean_audio_data

echo "Visualization"

python -m NLP.visualization

echo "  Transcription"
#python -m NLP.transcription /home/yesid/Desktop/mock_data/clean_audio_data/clean_audio.csv /home/yesid/Desktop/mock_data/transcription -l 'English'

echo  "Code executed successfully"
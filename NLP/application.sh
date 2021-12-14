#!/bin/bash

# create directory if not yet existing
mkdir -p data/clean_audio_data/
mkdir -p data/transcription/


echo "  Preprocessing"
#CHANGE THE FIRST PATH TO THE FOLDER WHERE THE RAW DATA ARE.
python -m NLP.audio_preprocessing data/raw_audio_data data/clean_audio_data


echo "  Transcription"
python -m NLP.transcription data/clean_audio_data/clean_audio.csv data/transcription -l 'English'

echo  "Code executed successfully"
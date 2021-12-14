## NLP
### How to use the code:
To run the preprocessing of the audio data and transcribe each audio file to text, 
follow these steps:
- Install the environment using the `VR.yml` file.
- Execute the file `application.sh`. This file executes the overall pipeline.
Store the raw data in a folder called `data/raw_audio_data` If you decide to store the data in a different location,
please change the path accordingly in the `application.sh`

### Audio preprocessing
The preprocessing of the audio files is done by running the script `audio_preprocessing.py`
The script parameters are the following:

- `input_dic`Path to the directory containing the raw audio data.
- `output_dic` Path to directory to save clean audio files and csv files. (These files are created automatically)

##### Output:
- Processed audio files (along with csv files listed below) are stored in the folder `data/clean_audio_data`.

- `clean_audio.csv` contains the participant's id, path to the (clean) audio files and audio's length.
- `audio_not_processed.csv` stores files, which due to a naming convention issue, will not be transcribed. 
These files must be checked manually. 

### Transcription
The transcription of the audio files is done by running the script `transcription.py`
The scripts parameters are the following:
- `input_csv` Path to csv file containing clean audio files. 
- `output_csv` Path to save  the csv with transcription.
- `l` or `--language` Indicate the language of transcription (English or German). Please change`application.sh` accordingly.

The transcriptions are stored in `data/transcription/transcription.csv`

## NLP
### How to use the code:
To run the preprocessing of the audio data and transcribe each file, 
follow these steps:
- Install the environment using the `VR.yml` file.
- In the terminal, run the file `audio.sh` to executes the overall pipeline.
  - Store the raw data in a folder called `data/raw_audio_data` If you decide to store the data in a different location,
please pass it as an argument to `audio.sh`. For example, if your data are store in `home/user/data`, run in the terminal
`bash audio.sh home/user/data`

### Audio preprocessing
The preprocessing of the audio files is done by running the script `audio_preprocessing.py`
The script parameters are the following:

- `input_dic`Path to the directory containing the raw audio data.
- `output_dic` Path to directory to save clean audio files and csv files. (These files are created automatically)

### Visualization
To generate visualizations of the data run the script `visualization.py`
The script parameters are the following:
- `dir_visualization` path to directory to store images/plots
- `clean_data` Path to the clean_audio.csv
- `not_processed` Path to audio_not_processed.csv

##### Output:
- Processed audio files (along with csv files listed below) are stored in the folder `data/clean_audio_data`.

- `clean_audio.csv` contains the participant's id, path to the (clean) audio files and audio's length.
- `audio_not_processed.csv` stores empty files as well as files with naming conventions. 
These files must be checked manually. 

### Transcription
The transcription of the audio files is done by running the script `transcription.py`
The scripts parameters are the following:
- `input_csv` Path to csv file containing clean audio files. 
- `output_csv` Path where the csv file containing the transcription is saved.
- `output_chunks` Path where the long-file chunks will be stored.
- `l` or `--language` Indicate the language of transcription (English or German). Please change`audio.sh` accordingly.

The transcriptions are stored in `data/transcription/transcription.csv`

#### Processing transcription

## Postural stability test


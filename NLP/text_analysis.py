import pandas as pd
import argparse

# setting up CLI



parser = argparse.ArgumentParser(description = "Text analysis")
parser.add_argument("transcription_csv", help = "path to the csv file containing the transcriptions")
parser.add_argument("output_dic", help = "path to the output directory")
args = parser.parse_args()


def create_text ():
    
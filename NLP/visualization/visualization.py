import pandas as pd
import matplotlib.pyplot as plt
import argparse



# setting up CLI

parser = argparse.ArgumentParser(description = "Visualization")
parser.add_argument("clean_data", help = "path to the clean_audio.csv")
parser.add_argument("not_processed", help = "path to audio_not_processed.csv")
args = parser.parse_args()

df_clean = pd.read_csv(args.clean_data)
df_not_processed= pd.read_csv(args.not_processed)


def visualize_raw_data(df_clean):
    plt.subplot(1,2,1)

    df_clean['duration_before_trim'].hist(bins=12)
    plt.title('Before_trimming')

    plt.subplot(1,2,2)
    df_clean['duration_after_trim'].hist(bins=13)
    plt.title('After_trimming')

    plt.suptitle('Duration')
    plt.xlabel('Seconds')
    plt.show()

visualize_raw_data(df_clean)
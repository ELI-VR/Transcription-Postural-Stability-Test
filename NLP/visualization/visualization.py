import pandas as pd
import matplotlib.pyplot as plt
import argparse



# setting up CLI

parser = argparse.ArgumentParser(description = "Visualization")
parser.add_argument("dir_visualization", help = "path to directory to store images plots")
parser.add_argument("clean_data", help = "path to the clean_audio.csv")
parser.add_argument("not_processed", help = "path to audio_not_processed.csv")
args = parser.parse_args()

df_clean = pd.read_csv(args.clean_data)
df_not_processed= pd.read_csv(args.not_processed)


def visualize_raw_data(df_clean,df_not_processed):
    fig, (ax1, ax2,ax3) = plt.subplots(1, 3)
    fig.suptitle('Data')
    ax1.hist(df_clean['duration_before_trim'])
    ax1.set_title('Duration before trimming',fontsize=8) #Duration before trimming
    ax1.set_xlabel('Seconds')

    ax2.hist(df_clean['duration_after_trim'])
    ax2.set_title('Duration after trimming',fontsize=8) #Duration after trimming
    ax2.set_xlabel('Seconds')

    ax3.hist(df_not_processed['issue'])
    ax3.set_title('Files_not_processed', fontsize=8)

    plt.savefig(f'{args.dir_visualization}/plot_data.png')
    plt.close(fig)


visualize_raw_data(df_clean,df_not_processed)
import pandas as pd
import os
import urllib.request
import sys


def download_conceptual(data_file):
    """
      Download Conceptual 12M dataset
      File is structured in .tsv format ([image_url]'\t'[image_caption])

      :param data_file: File to download data
      :type data_file: String
    """
    df = pd.read_csv(data_file, sep='\t', names=['url', 'caption'])

    dir = 'image-and-text-data'
    if not os.path.isdir(dir):
        os.mkdir(dir)

    x = 0
    for i in range(len(df['url'])):
        try:
            target_file = os.path.join(dir, f'conceptualcc12m_{x}')
            x += 1
            urllib.request.urlretrieve(
                df['url'].iloc[i], f'{target_file}.jpg')
            f = open(f'{target_file}.txt', 'w+')
            f.write(df['caption'].iloc[i])
            f.close()
        except Exception as e:
            print(f'An Exception has occured: {e}')


if __name__ == '__main__':
    """
        In order for this code to work, please make sure to download the 
        .tsv file from the following link: https://storage.googleapis.com/conceptual_12m/cc12m.tsv
    """
    download_conceptual('cc12m.tsv')
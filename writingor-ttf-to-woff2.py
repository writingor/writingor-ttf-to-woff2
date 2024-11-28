import os
import subprocess
from fontTools.ttLib.woff2 import compress


def convert():
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.ttf'):
            # prepare paths
            ttf_path = os.path.join(os.getcwd(), filename)
            woff2_path = os.path.splitext(ttf_path)[0] + '.woff2'
            # convert
            compress(ttf_path, woff2_path)
            print('Sucsessfully converted:', filename, 'to woff2')


if __name__ == '__main__':
    convert()
    print('Done')


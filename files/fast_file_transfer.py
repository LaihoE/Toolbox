import shutil
import os
from multiprocessing import Pool

in_folder = 'F:/csgo/turbo2/npz/'
files = os.listdir(in_folder)


def filemover(i):
    try:
        shutil.copy(f"{in_folder}{files[i]}",f"F:/csgo/npz_clean1/{files[i]}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    p = Pool(22)
    fs = len(files)
    p.map(filemover, range(fs))
import os
import numpy as np

in_folder = 'D:/f/democlipping/parsing/numpy/'
out_file = 'D:/nambibig/a'     # no .npy

def array_concatenator(in_folder,out_file):
    files = os.listdir(in_folder)
    a = np.concatenate([np.load(f"{in_folder}{file}")['arr_0'] for file in files])
    print(a.shape)
    np.save(out_file)


if __name__ == "__main__":
    array_concatenator(in_folder,out_file)
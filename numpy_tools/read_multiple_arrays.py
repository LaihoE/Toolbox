import os

import numpy as np

folder = 'D:/nampi/'
out_big_file = 'D:/nambibig/a'     # no .npy

files = os.listdir(folder)
files = files[:5000]
for cnt,file in enumerate(files):
    if cnt == 0:
        big = np.load(f"{folder}{file}")
    else:
        a = np.load(f"{folder}{file}")
        big = np.concatenate((big,a))
    print(cnt)
    
np.save(out_big_file)
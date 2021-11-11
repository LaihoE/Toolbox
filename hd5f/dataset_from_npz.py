import numpy as np
import os
import h5py


files = os.listdir(r"D:\output_processed\npz\clean/")
with h5py.File('D:/hd5/train_cheaters.h5', 'w') as hf:
    group = hf.create_group('group1')
    y = []
    for i in files:
        a = np.load(f"D:/output_processed/npz/clean/{i}")['arr_0']
        print(a.shape)
        y.append(a.shape[0])
        a = np.float32(a)
        a = a[:1000000,:,1:]
        group.create_dataset(f'{i}', data = a)
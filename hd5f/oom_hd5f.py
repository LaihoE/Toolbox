import os
import time

import joblib
import tables
import numpy as np
from sklearn.preprocessing import StandardScaler



hdf5_path = "D:/hd5/data9.hdf5"
def create():
    hdf5_file = tables.open_file(hdf5_path, mode='w')
    filters = tables.Filters(complevel=1, complib='blosc')

    #sample_data = np.load(r'D:\area51\multip\dasker\big3/0.npz')['arr_0']
    data_storage = hdf5_file.create_earray(hdf5_file.root, 'data',
                                          tables.Atom.from_dtype(np.dtype('float32')),
                                          shape=(0,128,5),
                                          filters = filters,
                                          chunkshape=(1,128,5))

    try:
        in_folder = 'F:/hd5f/dirty_train/'
        files = os.listdir(in_folder)
        for inx in range(1000):
            sub_files = files[inx*8000:inx*8000+8000]
            a = np.concatenate([np.load(f"{in_folder}{file}")["arr_0"] for file in sub_files])
            a = a[:, :, 1:]
            a = np.float32(a)
            data_storage.append(a)
    except Exception as e:
        print(e)

    in_folder = 'F:/hd5f/clean_train/'
    files = os.listdir(in_folder)
    for inx in range(1000):
        sub_files = files[inx * 5:inx * 5 + 5]
        a = np.concatenate([np.load(f"{in_folder}{file}") for file in sub_files])
        a = a[:, :, 1:]
        a = np.float32(a)
        data_storage.append(a)
    hdf5_file.close()


hdf5_file = tables.open_file(hdf5_path, mode='r')
print(hdf5_file)
a = time.time()


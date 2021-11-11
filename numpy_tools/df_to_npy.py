import numpy as np
import pandas as pd
import os
import time

folder = 'D:/unzipping/data/'
out_folder = 'D:/nampi/'

files = os.listdir(f"{folder}")
bigdf = pd.DataFrame()
dfs = []

for file in files:
    try:
        df = pd.read_csv(f"{folder}/{file}",header=None)
        df = df.to_numpy()
        np.save(f"{out_folder}{file}", df)
    except Exception:
        pass
bigdf = bigdf.append(dfs)
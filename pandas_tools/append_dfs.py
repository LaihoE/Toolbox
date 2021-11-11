import os
import pandas as pd
import time


now = time.time()

folder = 'D:/csgo/clean32/a/'
out_file = 'D:/newdata/clean.csv'
files = os.listdir(folder)
for i in files:
    df = pd.read_csv(f'{folder}{i}',header=None)
    df.to_csv(out_file, mode='a')

print(time.time() - now)

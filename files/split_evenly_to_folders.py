import os
import shutil
import math


folder = "D:/clean"
files = os.listdir(folder)
per_folder = 200

for i in range(math.ceil(len(files) / per_folder)):
    os.mkdir(f'{folder}/{i}')
    for j in range(per_folder*i,per_folder*i+per_folder):
        shutil.move(f'{folder}/{files[j]}',f'{folder}/{i}/{files[j]}')
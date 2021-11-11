import time

import numpy as np
import os

def matcher(a, ids):
    l = []
    for i in range(a.shape[0]):
        l.append(a[i][0][0])
    ids = set(ids)
    inxes = []
    for inx, i in enumerate(l):
        if i in ids:
            inxes.append(inx)
    return a[inxes]


files = os.listdir(r'I:\Shared drives\Demo 1\processed\faceit-clean')
#files = os.listdir(r'I:\Shared drives\Demo 1\clean\faceit')
files = [x.split('_')[-1] for x in files]
ids = [int(x.split('.')[0]) if len(x.split('.')[0]) >10 and len(x.split('.')[0]) < 19 else 42 for x in files]
print(ids)

a = np.load("D:/nambibig/real.npz")['arr_0']
now = time.time()
print(matcher(a, ids).shape)
print(time.time()-now)
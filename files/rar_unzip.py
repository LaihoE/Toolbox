from pyunpack import Archive
import os

folder = "C:/Users/emill/PycharmProjects/Toolbox/files/r"
outfolder = 'C:/Users/emill/PycharmProjects/Toolbox/files/unrar/'
files = os.listdir(folder)
print(files)
for x in files:
    Archive(f'{folder}/{x}').extractall(outfolder)
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import hashlib
import pandas as pd

# https://github.com/aadil494/youtube/blob/master/DetectAndDeleteDuplicateFiles/main.py

path_dan = r'\\DS220J\homes\Daniel\Photos'
path_li = r'\\DS220J\homes\Lisa\Photos'
path_li_mom = r'\\DS220J\homes\Lisa_Mom\Photos'
path_share = r'\\DS220J\photo'

file2hash = []


def hash_path(path):
    for folder, sub_folder, files in os.walk(path):
        for file in files:
            filePath = os.path.join(folder, file)
            fileHash = hashlib.md5(open(filePath, 'rb').read()).hexdigest()
            print(filePath)
            file2hash.append([filePath, fileHash])
    return file2hash


hash_path(path_share)
hash_path(path_li)
hash_path(path_dan)
hash_path(path_li_mom)
df = pd.DataFrame(file2hash, columns=['path', 'hash'])
df_dup = df.loc[df['hash'].duplicated(keep='first')]

#
# df = pd.DataFrame(file2hash, columns=['path', 'hash'])
# df_dup = df.loc[df['hash'].duplicated(keep=False)]
# df_dup.to_csv('duplicated_list.csv')

#
# if fileHash in uniqueFiles:
#     os.remove(filePath)
#     print("Removing...:", filePath)
# else:
#     uniqueFiles[fileHash] = path_dan

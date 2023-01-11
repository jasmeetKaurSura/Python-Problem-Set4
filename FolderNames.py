# this file fetch all files in the given base path in your computer
import os
from os import scandir
       
def fileName(path):
    sub_entries = os.scandir(path)
    for sub_entry in sub_entries:
        if sub_entry.is_dir():
            pathx= path +"/"+ sub_entry.name
            fileName(pathx)
        else:
            print(path + sub_entry.name)

basePath = 'Desktop'
fileName(basePath)
   

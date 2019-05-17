## collecting
#1. list file name+path with regex file name
#2. read lines
#3. storage
import os
from os import walk
import pprint

file_list = []
dir_list=[]
pp = pprint.PrettyPrinter(indent=4)
PATH = 'C:\\test\\angular\\remote\\springboot_angular\\demo\\src\\test'

for root, dirs, files in walk(PATH):
    for file in files:
        file_list.append(os.path.join(root, file))
    # file_list.extend(files)
    # dir_list.extend(dirs)
for file in files:

    pp.pprint(file)
pp.pprint(file_list)
pp.pprint(dir_list)

########################
def file_name_filter(path=""):
   
    if( os.path.basename(path).find('Excep') == -1):
        return False
    else:
        return True



## reformat


## output
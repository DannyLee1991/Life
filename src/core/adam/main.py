__author__ = 'lijianan'

import os
import random
import shutil
import sys
import time

from src.utils.utlis import GetParentPath, modify_file

time.sleep(1)
print("=================new one comming!===================================")


def getDirPath(index):
    dir = GetParentPath(sys.path[0])
    if not index:
        index = ""
    dir += os.sep + "adam" + str(index)
    return dir


def getNum():
    file = open('index.py', 'r')
    line = file.readline()
    try:
        num = int(line)
        file.close()
        return num
    except ValueError:
        file.close()
        return 0


# get current file name : main.py
current_file_name = sys.argv[0][sys.argv[0].rfind(os.sep) + 1:]
# get current adam index number
index = getNum()

current_dir = getDirPath(index) + os.sep
print("current index ==> " + str(index))
index += 1
next_dir = getDirPath(index) + os.sep
print("generate index ==> " + str(index))

# create file and copy file
if not os.path.exists(next_dir):
    os.mkdir(next_dir)
self_path = current_dir + current_file_name
new_one_path = next_dir + current_file_name
print("self path ==> " + self_path)
print("next path ==> " + new_one_path)
shutil.copyfile(self_path, new_one_path)

# change local index number in index.py file
modify_file('index.py', str(index))

# give info
print("execute give info ===> ")
info_file = open(next_dir + "info.py", "w")
info = [
    "__author__ = 'lijianan'",
    os.linesep,
    os.linesep,
    "static_info = {",
    os.linesep,
    "   'species':'human',",
    os.linesep,
    "   'breathday':'" + str(time.time()) + "' ",
    os.linesep,
    "}",
    os.linesep,
    os.linesep,
    "dynamic_info = {",
    os.linesep,
    "   'sex':" + str(random.randint(0, 1)) + ", # 0 is male,1 is female",
    os.linesep,
    "   'age':" + str(random.randint(0, 100)) + ",",
    os.linesep,
    "}"
]
info_file.writelines(info)

print(new_one_path + " is created!")

# give life to next adam
os.system("python " + new_one_path)

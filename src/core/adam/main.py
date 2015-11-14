__author__ = 'lijianan'
import os,sys,time,shutil
from src.utils.utlis import GetParentPath,modify_file

time.sleep(1)
print("=================new one comming!===================================")

def getDirPath(index):
    dir = GetParentPath(sys.path[0])
    if not index:
        index = ""
    dir += os.sep + "adam" + str(index)
    return dir

def getNum():
    file = open('../index.py','r')
    line = file.readline()
    try:
        num = int(line)
        file.close()
        return num
    except ValueError:
        file.close()
        return 0

current_file_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
index = getNum()

current_dir = getDirPath(index) + os.sep
index += 1
print("current index ==> " + str(index))
next_dir = getDirPath(index) + os.sep

if not os.path.exists(next_dir):
    os.mkdir(next_dir)
new_one_path = next_dir + current_file_name

self_path = current_dir + current_file_name
print("self path ==> " + self_path)
print("next path ==> " + new_one_path)
shutil.copyfile(self_path,new_one_path)

modify_file('../index.py',str(index))
# give info
print(new_one_path + " is created!")

# give life
os.system("python " + new_one_path)

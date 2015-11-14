__author__ = 'lijianan'
import os

def GetParentPath(strPath):
    if not strPath:
        return None;

    lsPath = os.path.split(strPath);
    if lsPath[1]:
        return lsPath[0];

    lsPath = os.path.split(lsPath[0]);
    return lsPath[0];

def modify_file(file,rstr):
    try:
        index_file = open(file,'w')
        index_file.write(str(rstr))
        index_file.close()
    except Exception,e:
        print e


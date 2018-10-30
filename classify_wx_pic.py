#coding:utf8
import os
import imghdr
import shutil
import time

path = u'E:\\日常\\兜兜wx'
dst_path = u'E:\\日常\\兜兜图像格式化'

def getFileTmStruct(abs_file):
    tm = os.path.getmtime(abs_fs)
    return getYearAndMonth(tm)    

def getYearAndMonth(ts):
    time_struct = time.localtime(ts)
    return time_struct

def createDir(file):
    ldir = os.path.abspath(file)
    if not os.path.exists(ldir):   
        os.makedirs(ldir) 

if __name__ == '__main__':
    fss = os.listdir(path)
    index = 1
    for fs in fss:
        abs_fs = os.path.join(path,fs)
        tm_struct = getFileTmStruct(abs_fs)
        pv_path = os.path.join(dst_path, str(tm_struct.tm_year), str(tm_struct.tm_mon)+u'月')
        if imghdr.what(abs_fs):
            dst_file = os.path.join(pv_path, 'pic')
            createDir(dst_file)
        else:
            dst_file = os.path.join(pv_path, 'video')
            createDir(dst_file) 

        print dst_file   
        shutil.copy(abs_fs, dst_file)
        print abs_fs
        if index > 5:
            break
        index += 1  


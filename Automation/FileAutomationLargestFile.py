from sys import *
import os
import time

def directoryTravel(dirName):
    print('we are goint to travel the directory', dirName)
    flag = os.path.isabs(dirName)
    if (flag == False):
        dirName = os.path.abspath(dirName)
    
    isExists = os.path.isdir(dirName)
    if (isExists == False):
        return

    maxFile = ''
    maxsize = 0
    for folderName, subFolderName, fileName in os.walk(dirName):
        for fname in fileName:
            currentFile = os.path.join(folderName, fname)
            size = os.path.getsize(currentFile)
            if (size > maxsize):
                maxsize = size
                maxFile = currentFile

    print('max size file is', maxFile, 'with size', maxsize)

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to perform the File Automations')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(FileName)')
        print('Example : Demo.py HelloWorld')
        exit()
    else:
        startTime = time.time()
        directoryTravel(argv[1])
        endTime = time.time()

        print ('The script took time to execute as :', endTime - startTime)

if (__name__ == '__main__'):
    main()

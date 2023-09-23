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

    for folderName, subFolderName, fileName in os.walk(dirName):
        count = 1
        for fname in fileName:
            currentFile = os.path.join(folderName, fname)
            split_tup = os.path.splitext(fname)
            newName = os.path.join(folderName, str(count)+split_tup[1])
            os.rename(currentFile, newName)
            count = count + 1
            
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

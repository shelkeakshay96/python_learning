from sys import *
import os
import Logger

def displayFiles(dirName, extentionName, renameExtention):
    flag = os.path.isabs(dirName)
    if flag == False:
        dirName = os.path.abspath(dirName)

    exists = os.path.isdir(dirName)

    if exists == False:
        print('Directory {} does not exists'. format(dirName))
        return

    for folderName, subFolderName, fileName in os.walk(dirName):
        if (folderName != dirName):
            break
        for fname in fileName:
            fileWithPath = os.path.join(folderName, fname)
            split_tup = os.path.splitext(fileWithPath)
            if (split_tup[1] == extentionName):
                os.rename(fileWithPath, os.path.join(folderName, split_tup[0]+renameExtention))

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to Replace file extentions')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(FileName)')
        print('Example : Demo.py .txt .log')
        exit()
    elif len(argv) < 4:
        print('Invalid number of arguments')
        exit()
    else:
        displayFiles(argv[1], argv[2], argv[3])

if (__name__ == '__main__'):
    main()

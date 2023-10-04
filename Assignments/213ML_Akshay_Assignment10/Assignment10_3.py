from sys import *
import os
import shutil

def copyFolderFiles(sourceFolder, destinationFolder):
    flag = os.path.isabs(sourceFolder)
    if flag == False:
        sourceFolder = os.path.abspath(sourceFolder)

    exists = os.path.isdir(sourceFolder)

    if exists == False:
        print('Directory {} does not exists'. format(sourceFolder))
        return
    
    flag = os.path.isabs(destinationFolder)
    if flag == False:
        destinationFolder = os.path.abspath(destinationFolder)

    existsDestFolder = os.path.isdir(destinationFolder)
    if existsDestFolder == False:
        os.mkdir(destinationFolder)

    for folderName, subFolderName, fileName in os.walk(sourceFolder):
        if (folderName != sourceFolder):
            break
        for fname in fileName:
            fileWithPath = os.path.join(folderName, fname)
            destFile = os.path.join(destinationFolder, fname)
            shutil.copy(fileWithPath, destFile)

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to Copy File To New Folder')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(FolderName) Second_Argument(FolderName)')
        print('Example : Demo1 Demo2')
        exit()
    elif len(argv) < 3:
        print('Invalid number of arguments')
        exit()
    else:
        copyFolderFiles(argv[1], argv[2])

if (__name__ == '__main__'):
    main()

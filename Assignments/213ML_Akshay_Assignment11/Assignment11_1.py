from sys import *
import os
import hashlib
import Logger

def displayFiles(dirName):
    flag = os.path.isabs(dirName)
    if flag == False:
        dirName = os.path.abspath(dirName)

    exists = os.path.isdir(dirName)

    if exists == False:
        print('Directory {} does not exists', format(dirName))
        return

    for folderName, subFolderName, fileName in os.walk(dirName):
        if (folderName != dirName):
            break
        for fname in fileName:
            currentFile = os.path.join(folderName, fname)
            fileCheckSum = hashlib.md5(open(currentFile,'rb').read()).hexdigest()
            logginContent = 'Checksum for {} => {}'. format(currentFile, fileCheckSum)
            Logger.log(logginContent)

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to Display File checksum')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(DirectoryName)')
        print('Example : Demo')
        exit()
    else:
        displayFiles(argv[1])

if (__name__ == '__main__'):
    main()

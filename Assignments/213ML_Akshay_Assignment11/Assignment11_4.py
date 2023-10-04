from sys import *
import os
import time
import hashlib
import Logger

def deleteDuplicateFiles(dirName):
    flag = os.path.isabs(dirName)
    if flag == False:
        dirName = os.path.abspath(dirName)

    exists = os.path.isdir(dirName)

    if exists == False:
        print('Directory {} does not exists', format(dirName))
        return

    setOfFiles = set()
    for folderName, subFolderName, fileName in os.walk(dirName):
        if (folderName != dirName):
            break
        for fname in fileName:
            currentFile = os.path.join(folderName, fname)
            fileCheckSum = hashlib.md5(open(currentFile,'rb').read()).hexdigest()
            if fileCheckSum in setOfFiles:
                os.remove(currentFile)
                Logger.log('Deleted File {} from the directory'. format(currentFile))
            else:
                setOfFiles.add(fileCheckSum)

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to Delete duplicate file and calculate execution time')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script
        print('Usage : Name_Of_Script First_Argument(DirectoryName)')
        print('Example : Demo')
        exit()
    else:
        startTime = time.time()
        deleteDuplicateFiles(argv[1])
        endTime = time.time()

        Logger.log('The script took time to execute as : {}'. format(endTime - startTime))

if (__name__ == '__main__'):
    main()

from sys import *
import os
import time

def copyFile(search):
    for folderName, subFolderName, fileName in os.walk(os.getcwd()):
        for fname in fileName:
            currentFile = os.path.join(folderName, fname)
            if (fname == search):
                print('file found at : ', currentFile)

                try:
                    readInputFile = open(currentFile, 'r')

                    newFilePath = os.path.join(folderName, 'Demo.txt')
                    writeFile = open(newFilePath, 'w')
                    writeFile.write(readInputFile.read())
                    print('File copied successfully at', newFilePath)
                    readInputFile.close()
                    writeFile.close()
                except OSError as E:
                    print('File operations failed! ', E)

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to Copy input file contents to Demo.txt file')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(FileName)')
        print('Example : Demo.py')
        exit()
    else:
        startTime = time.time()
        copyFile(argv[1])
        endTime = time.time()

        print ('The script took time to execute as :', endTime - startTime)

if (__name__ == '__main__'):
    main()

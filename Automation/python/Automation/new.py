from sys import *
import os

def directoryTravel(dirName):
    print('we are goint to travel the directory', dirName)

    for folderName, subFolderName, fileName in os.walk(dirName):
        for fname in fileName:
            print(fname)

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
        directoryTravel(argv[1])

if (__name__ == '__main__'):
    main()

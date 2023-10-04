from sys import *
import os
import time

def readFile(inputFilename, searchWord):
    wordCount = 0
    for folderName, subFolderName, fileName in os.walk(os.getcwd()):
        for fname in fileName:
            if (fname == inputFilename):
                with open(os.path.join(folderName, fname),'r') as file:
                    for line in file:
                        for word in line.split():
                            if (word == searchWord):
                                wordCount+= 1

    return wordCount

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('Check 2 files are equal')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(FileName) Second_Argument(Word to Search)')
        print('Example : Demo1.py Akshay')
        exit()
    elif (len(argv) < 3):
        print('Invalid number of arguments')
    else:
        startTime = time.time()
        foundCount = readFile(argv[1], argv[2])
        print('word {} found at {} time in file.'. format(argv[2], foundCount))
        endTime = time.time()

        print ('The script took time to execute as :', endTime - startTime)

if (__name__ == '__main__'):
    main()

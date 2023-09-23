from sys import *
import os
import hashlib
import time

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()    

def displayCheckSum(path):
    flag = os.path.isabs(path)
    if (flag == False):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if (exists):
        for dirName, subdirs, fileList in os.walk(path):
            print('Current folder is: '+ dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
        print('Error : Invalid number of arguments')
        exit()
    
    if (argv[1] == "-h") or (argv[1] == '-H'):
        print('This script is used to traverse specific directory')
        exit()

    if (argv[1] == "-h") or (argv[1] == '-H'):
        print('Usage : ApplicationName Absolute_of_Directory')
        exit()

    try:
        DirectoryWatcher(argv[1])
    except ValueError:
        print('Error: Invalid datatype of Input')
    except Exception:
        print('Error: Invalid Input')

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to Traverse specific directory and disaplay cec')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(FileName)')
        print('Example : Demo.py HelloWorld')
        exit()
    else:
        try:
            startTime = time.time()
            arr = displayCheckSum(argv[1])
            endTime = time.time()
            print ('The script took time to execute as :', endTime - startTime)
        except ValueError:
            print('Error : Invalid datatype of input')

        except Exception as E:
            print('Error : Invalid input', E)


if (__name__ == '__main__'):
    main()

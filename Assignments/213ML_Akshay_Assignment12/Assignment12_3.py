import psutil
import Logger
from sys import *

def getRunningProcesses():
    processList = list()
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'username', 'name'])
            processList.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processList

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to check and log running processes in specific folder')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(Directory Name where log file is located)')
        print('Example : Demo.py Demo')
        exit()
    else:
        process = getRunningProcesses()
        for p in process:
            Logger.log(p, argv[1])

if __name__=="__main__":
    main()

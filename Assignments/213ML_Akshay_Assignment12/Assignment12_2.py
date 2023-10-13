import psutil
import Logger
from sys import *

def isProcessRunning(processInputName):
    isRunning = False
    if (processInputName == ''):
        return isRunning

    if (processInputName.find('.exe') == -1):
        processInputName = processInputName + '.exe'

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'username', 'name'])
            if (pinfo['name'].lower() == processInputName):
                isRunning = True
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return isRunning

def main():
    if (len(argv) < 2):
        print('Invalid number of arguments')
        exit()

    if argv[1] in ['-h', '-H']:  # Flag for help of script
        print('This script is used to check and log if specific process is running or not')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(ProcessName) ')
        print('Example : Demo.py Notepad')
        exit()
    else:
        process = argv[1]
        if isProcessRunning(process.lower()):
            Logger.log('The Process "{}" is running!'. format(process))
        else:
            Logger.log('The Process "{}" is NOT running!'. format(process))

if __name__=="__main__":
    main()

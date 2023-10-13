import psutil
import Logger
from sys import *
import time
import Mailer

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
        print('This script is used to Send log file over an email')
        exit()
    elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
        print('Usage : Name_Of_Script First_Argument(Directory Name where log file is located) Second_Argument(email) ')
        print('Example : Demo.py Demo demo@mail.com')
        exit()
    elif (len(argv) < 3):
        print('Invalid number of arguments')
        exit()
    else:
        process = getRunningProcesses()
        fileName = ''
        for p in process:
            fileName = Logger.log(p, argv[1])

        currentTime = time.ctime()
        Mailer.send_mail_with_attachment(
            toaddr = argv[2],
            subject ="""
            Process log : generated at : %s
            """%(currentTime),
            body = """
            Hello,
            Attached the process log file
            Log file is created at : %s
                """ %(currentTime),
            filename = fileName
        )

if __name__=="__main__":
    main()

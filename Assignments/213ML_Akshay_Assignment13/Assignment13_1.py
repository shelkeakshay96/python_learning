from sys import *
import os
import time
import hashlib
import schedule
import Logger
import Mailer
from datetime import datetime

def deleteDuplicateFiles(dirName):
    startTime = time.time()
    flag = os.path.isabs(dirName)
    if flag == False:
        dirName = os.path.abspath(dirName)

    exists = os.path.isdir(dirName)

    if exists == False:
        print('Directory {} does not exists', format(dirName))
        return

    setOfFiles = set()
    logFileName = ''
    scannedCount = 0
    deletedCount = 0
    for folderName, subFolderName, fileName in os.walk(dirName):
        if (folderName != dirName):
            break
        for fname in fileName:
            currentFile = os.path.join(folderName, fname)
            fileCheckSum = hashlib.md5(open(currentFile,'rb').read()).hexdigest()
            if fileCheckSum in setOfFiles:
                # os.remove(currentFile)
                deletedCount+= 1
                logFileName = Logger.log('Deleted File {} from the directory'. format(currentFile))
            else:
                setOfFiles.add(fileCheckSum)
            scannedCount+= 1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if (logFileName and deletedCount > 0 ):
        Mailer.send_mail_with_attachment(
            toaddr = argv[3],
            subject ="""
            Duplicate Removal log : generated at : %s
            """%(now),
            body = """
            Hello,
            Attached the Duplicate Removal log file
            Log file is created at : %s
            Total number of files scanned : %s
            Total number of duplicate files found and deleted : %s
                """ %(now, scannedCount, deletedCount),
            filename = logFileName
        )

    endTime = time.time()
    fileName = Logger.log('The script took time to execute as : {}'. format(endTime - startTime))

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
    elif (len(argv) < 4):
        print('Invalid number of arguments')
        exit()
    else:
        schedule.every(float(argv[2])).minutes.do(deleteDuplicateFiles, argv[1])
    
    while(True):
        schedule.run_pending()
        time.sleep(1)

if (__name__ == '__main__'):
    main()

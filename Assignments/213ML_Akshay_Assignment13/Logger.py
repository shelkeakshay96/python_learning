import os
from datetime import datetime

def log(line = '', dirPath = 'Marvellous'):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    flag = os.path.isabs(dirPath)
    if flag == False:
        dirPath = os.path.abspath(dirPath)

    exists = os.path.isdir(dirPath)
    if (exists == False):
        os.mkdir(dirPath)
    logFileName = "DuplicateRemovalLog_%s.log" %(now)
    fileName = os.path.join(dirPath , logFileName)
    f = open(fileName, "a")
    line = str(line) + "\n"
    log = '[{}] {}'. format(now, line)
    f.write(log)
    f.close()

    return fileName

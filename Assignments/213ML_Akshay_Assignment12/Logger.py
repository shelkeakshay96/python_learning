import os
from datetime import datetime

def log(line = '', dirPath = 'Demo'):
    now = datetime.now()

    flag = os.path.isabs(dirPath)
    if flag == False:
        dirPath = os.path.abspath(dirPath)

    exists = os.path.isdir(dirPath)
    if (exists == False):
        os.mkdir(dirPath)

    fileName = os.path.join(dirPath , 'assignment.log')
    f = open(fileName, "a")
    line = str(line) + "\n"
    log = '[{}] {}'. format(now, line)
    f.write(log)
    f.close()

    return fileName

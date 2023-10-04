import os

def isFileExists(ipFileName):
    found = False
    for folderName, subFolderName, fileName in os.walk(os.getcwd()):
        for fname in fileName:
            if (fname == ipFileName):
                found = True
                break
        if (found):
            break

    if (found):
        return 'Exists'
    else:
        return 'NOT Exists'

def main():
    print('Check whether file exists in current directory or not')
    fileName = str(input('Enter a file name : '))
    print('File {} {} in current folder'. format(fileName, isFileExists(fileName)))
    
if (__name__ == '__main__'):
    main()

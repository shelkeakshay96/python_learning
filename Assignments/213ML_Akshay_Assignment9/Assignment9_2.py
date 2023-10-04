import os

def readFile(ipFileName):
    found = False
    for folderName, subFolderName, fileName in os.walk(os.getcwd()):
        for fname in fileName:
            if (fname == ipFileName):
                currentFile = os.path.join(folderName, fname)
                found = True
                print('File found at :', currentFile)
                print('Contents of file :')
                print('---')

                f = open(currentFile, "r")
                print(f.read())
                f.close()
                print('---')
                break
        if (found):
            break

    if (found == False):
        print('File not found')
    

def main():
    print('Check whether file exists in current directory or not')
    fileName = str(input('Enter a file name : '))
    readFile(fileName)
    
if (__name__ == '__main__'):
    main()

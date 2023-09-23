from sys import *
from Arithematic import *

def main():
    if (len(argv) == 2):
        if argv[1] in ['-h', '-H']:  # Flag for help of script
            print('This script is used to perform the addion on 2 numbers')
            exit()
        elif argv[1] in ['-u', '-U']:  # Flag for usage of script 
            print('Usage : Name_Of_Script First_Argument Second_Argument')
            print('Example : Demo.py 11 12')
            exit()
        else:
            print('There is no such case to handle')
            exit()

    if (len(argv) < 3):
        print('Invalid number of arguments')
        exit()
    else:
        print('Addition is :', addition(int(argv[1]), int(argv[2])))

if (__name__ == '__main__'):
    main()

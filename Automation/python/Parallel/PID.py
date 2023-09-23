import os

def main():
    print('Current Process Id : ' , os.getpid())   # will be static (process: terminal)
    print('Current Process Id : ' , os.getppid())  # Will change everytime (process: this program)

if (__name__ == '__main__'):
    main()
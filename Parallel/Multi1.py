import multiprocessing
import os
import time
import inspect

def task1(value1):
    print('Executing the',inspect.stack()[0][3],'task...')
    print('PID of parent process is', os.getppid())
    print('PID of running process is', os.getpid())

def task2(value1, value2):
    print(value1, value2)
    print('Executing the',inspect.stack()[0][3],'task...')
    print('PID of parent process is', os.getppid())
    print('PID of running process is', os.getpid())

def main():
    print('---Demonstration of Multiprocessing---')

    print('PID of parent process is', os.getppid())
    print('PID of running process is', os.getpid())
    no = 5
    no2 = 10

    # Serial programming
    # task1(no)
    # task2(no)

    # Parellel programming: (multiprocessing)
    p1 = multiprocessing.Process(target= task1, args=(no, ))
    p2 = multiprocessing.Process(target= task2, args=(no, no2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if (__name__ == '__main__'):
    main()

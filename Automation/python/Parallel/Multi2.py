import multiprocessing
import os
import time
import inspect

def task1(value1):
    print('Executing the',inspect.stack()[0][3],'task...')
    for i in range(value1):
        print('Task1 :', i)

def task2(value1):
    print('Executing the',inspect.stack()[0][3],'task...')
    for i in range(value1):
        print('Task2 :', i)

def main():
    print('---Demonstration of Multiprocessing---')
    no = 500
    no2 = 800

    # Parellel programming: (multi-processing)
    p1 = multiprocessing.Process(target= task1, args=(no,))
    p2 = multiprocessing.Process(target= task2, args=(no2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if (__name__ == '__main__'):
    main()

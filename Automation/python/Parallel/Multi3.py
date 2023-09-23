import os
import inspect
import threading

def task1(value1):
    print('Executing the',inspect.stack()[0][3],'task...')
    print('pid of', inspect.stack()[0][3], ':' , os.getpid())
    print('thread id of', inspect.stack()[0][3], ':' , threading.get_ident())
    for i in range(value1):
        print(inspect.stack()[0][3], ':', i)

def task2(value1):
    print('Executing the',inspect.stack()[0][3],'task...')
    print('pid of', inspect.stack()[0][3], ':' , os.getpid())
    print('thread id of', inspect.stack()[0][3], ':' , threading.get_ident())
    for i in range(value1):
        print(inspect.stack()[0][3], ':', i)

def main():
    print('---Demonstration of MultiThreading---')
    print('pid of', inspect.stack()[0][3], ':' , os.getpid())
    print('thread id of', inspect.stack()[0][3], ':' , threading.get_ident())
    no1 = 5
    no2 = 8

    # Parellel programming: (multi-processing)
    p1 = threading.Thread(target= task1, args=(no1,))
    p2 = threading.Thread(target= task2, args=(no2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if (__name__ == '__main__'):
    main()

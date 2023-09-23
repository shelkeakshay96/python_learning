import multiprocessing
import os
import time

def square(n):
    print("worker process id for {0} : {1}" . format (n, os.getpid()))
    return (n * n)

def main():
    print(os.cpu_count())
    arr = [1, 2, 3, 4, 5]
    print(arr)

    p = multiprocessing.Pool()
    start = time.time()
    result = p.map(square, arr)
    print('Square of each element is : ')
    print(result)
    end = time.time()
    print((end-start) * 10**3, "ms")

if (__name__ == '__main__'):
    main()

import threading

def printSerial():
    for i in range(1, 51):
        print(threading.current_thread().name, ':', i)

def printReverse():
    for i in range(50, 0, -1):
        print(threading.current_thread().name, ':', i)

def main():
    t1 = threading.Thread(target=printSerial, name='serial-thread')
    t2 = threading.Thread(target=printReverse, name='reverse-thread')

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if (__name__ == '__main__'):
    main()

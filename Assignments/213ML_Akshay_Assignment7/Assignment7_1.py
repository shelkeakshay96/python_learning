import threading

def printEven(nos):
    for i in nos:
        if (i % 2 == 0):
            print('Even no :', i)

def printOdd(nos):
    for i in nos:
        if (i % 2 != 0):
            print('Odd no :', i)

def accept():
    no = int(input('Enter length of list : '))
    listInput = []
    for i in range(no):
        listInput.append(int(input('Enter number to add in list : ')))
    return listInput

def main():
    listNumbers = accept()
    t1 = threading.Thread(target=printEven, args=(listNumbers, ))
    t2 = threading.Thread(target=printOdd, args=(listNumbers, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if (__name__ == '__main__'):
    main()

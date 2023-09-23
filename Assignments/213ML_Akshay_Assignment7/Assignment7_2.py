import threading

def evenFactor(no):
    sum = 0
    i = 1
    while (i <= no):
        if (i % 2 == 0 and no % i == 0):
            print('Even no :', i)
            sum = sum + i
        i = i + 1
    print('Even factors addition :', sum)

def oddFactor(no):
    sum = 0
    i = 1
    while (i <= no):
        if (i % 2 != 0 and no % i == 0):
            print('Odd no :', i)
            sum = sum + i
        i = i + 1
    print('Odd factors addition :', sum)

def accept():
    return int(input('Enter a number : '))

def main():
    no = accept()
    t1 = threading.Thread(target=evenFactor, args=(no, ))
    t2 = threading.Thread(target=oddFactor, args=(no, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('---Exit from main---')

if (__name__ == '__main__'):
    main()

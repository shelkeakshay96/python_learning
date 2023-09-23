import threading

def small(strInput):
    listSmall = []
    for i in strInput:
        if (i.islower()):
            listSmall.append(i)
    print ('list of small charaters :', listSmall)
    print('Id of', threading.current_thread().name ,':', threading.get_ident())

def capital(strInput):
    listCapital = []
    for i in strInput:
        if (i.isupper()):
            listCapital.append(i)
    print ('list of capital charaters :', listCapital)
    print('Id of', threading.current_thread().name ,':', threading.get_ident())

def degit(strInput):
    listDigit = []
    for i in strInput:
        if (i >= '0' and i <= '9'):
            listDigit.append(i)
    print ('list of digit charaters :', listDigit)
    print('Id of', threading.current_thread().name ,':', threading.get_ident())

def accept():
    return str(input('Enter a string : '))

def main():
    strInput = accept()
    t1 = threading.Thread(target=small, args=(strInput, ), name="small-thread")
    t2 = threading.Thread(target=capital, args=(strInput, ), name="capital-thread")
    t3 = threading.Thread(target=degit, args=(strInput, ), name="degit-thread")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if (__name__ == '__main__'):
    main()

import MarvellousNum

def primeAddition(nos):
    addition = 0
    for i in nos:
        addition = addition + i
    return addition

def listPrime(nos):
    listPrime = list()
    for i in range(len(nos)):
        if (MarvellousNum.chkPrime(nos[i])):
            listPrime.append(nos[i])
    return listPrime

def main():
    length = int(input('Number of elements : '))
    elements = list()

    for i in range(length):
        elements.append(int(input('Enter Element : ')))

    primeNos = listPrime(elements)
    
    print('List of prime :', primeNos)
    print('Addition of prime :', primeAddition(primeNos))

if (__name__ == '__main__'):
    main()

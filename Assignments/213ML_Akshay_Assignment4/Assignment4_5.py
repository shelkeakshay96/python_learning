from functools import reduce

def isPrime(no):
    isPrime = True
    for i in range(2, no):
        if (no % i == 0):
            isPrime = False
            break
    return isPrime

def getMax(no1, no2):
    if (no1 > no2):
        return no1
    else:
        return no2

def main():
    no = int(input('Enter a length of a list : '))
    elements = list()
    for i in range(no):
        elements.append(int(input('Enter element : ')))
    print('Input List = {}'. format(elements))

    listFilter = list(filter(isPrime, elements))
    print(listFilter)

    listMap = list(map(lambda i: i * 2, listFilter))
    print(listMap)

    max = reduce(getMax, listMap)
    print(max)

if (__name__ == '__main__'):
    main()

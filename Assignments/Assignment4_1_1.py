from functools import reduce

def inputList():
    listOfTwo = list()
    for i in range(int(input('Enter a number : '))):
        listOfTwo.append(2)
    return listOfTwo

def main():
    listOfTwo = inputList()

    power = reduce(lambda no1, no2 : no1 * no2, listOfTwo)
    print(power)

if (__name__ == '__main__'):
    main()

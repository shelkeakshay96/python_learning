def checkEven(no):
    if (no%2 == 0):
        return True
    else:
        return False
    
def increaseByTwo(no):
    return no + 2

def add(a, b):
    return a + b

def main():
    data = [5, 4, 9, 8, 13, 17, 12, 18]
    result = []
    addition = 0

    for i in data:
        if (checkEven(i)):  #Filter
            result.append(increaseByTwo(i))  #Map

    for i in result: #Reduce
        addition = addition + i

    print('addition : ', addition)


if (__name__ == '__main__'):
    main()


import functools 

def checkEven(no):
    return (no%2 == 0)
    
def increaseByTwo(no):
    return no + 2

def add(a, b):
    return a + b

def main():
    data = list()
    no = int(input('Enter length of list elements : '))
    for i in range(no):
        data.append(int(input('Enter list element : ')))
    
    print('list is :', data)

    output = list(filter(checkEven, data))
    moutput = list(map(increaseByTwo, output))
    result = functools.reduce(add, moutput)

    print(output)
    print(moutput)
    print(result)


if (__name__ == '__main__'):
    main()

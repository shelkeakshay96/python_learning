def listAddition(nos):
    addition = 0
    for i in nos:
        addition = addition + i

    return addition

def main():
    length = int(input('Number of elements : '))
    elements = list()
    
    for i in range(length):
        elements.append(int(input('Enter Element : ')))
    
    print('List is : ', elements)
    print('Addition is :', listAddition(elements))
    

if (__name__ == '__main__'):
    main()

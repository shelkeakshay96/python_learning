def listMax(nos):
    max = nos[0]
    for i in range(len(nos)):
        if(nos[i] > max):
            max = nos[i]

    return max

def main():
    length = int(input('Number of elements : '))
    elements = list()
    
    for i in range(length):
        elements.append(int(input('Enter Element : ')))
    
    print('List is :', elements)
    print('Max number is :', listMax(elements))
    
if (__name__ == '__main__'):
    main()

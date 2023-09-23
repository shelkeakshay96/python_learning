def listMin(nos):
    min = nos[0]
    for i in range(len(nos)):
        if (min > nos[i]):
            min = nos[i]

    return min

def main():
    length = int(input('Number of elements : '))
    elements = list()
    
    for i in range(length):
        elements.append(int(input('Enter Element : ')))
    
    print('List is :', elements)
    print('Min number is :', listMin(elements))
    
if (__name__ == '__main__'):
    main()

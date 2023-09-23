def listFrequencyCount(nos, no):
    frequencyCount = 0
    for i in range(len(nos)):
        if (no == nos[i]):
            frequencyCount = frequencyCount + 1

    return frequencyCount

def main():
    length = int(input('Number of elements : '))
    elements = list()

    for i in range(length):
        elements.append(int(input('Enter Element : ')))

    searchNo = int(input('Enter number to search : '))

    print('List is :', elements)
    print('Frequency of element', searchNo, 'is :', listFrequencyCount(elements, searchNo), 'times')

if (__name__ == '__main__'):
    main()

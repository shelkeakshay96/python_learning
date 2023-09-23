from functools import reduce

def main():
    no = int(input('Enter a length of a list : '))
    elements = list()
    for i in range(no):
        elements.append(int(input('Enter element : ')))
    print('Input List = {}'. format(elements))
    
    listEven = list(filter(lambda no: (no % 2 == 0), elements))
    print('List after filter = {}'. format(listEven))

    listSquare = list(map(lambda no: no ** 2, listEven))
    print('List after map = {}'. format(listSquare))

    addition = reduce(lambda i, j: i + j, listSquare)
    print('Output of reduce = {}'. format(addition))
if (__name__ == '__main__'):
    main()

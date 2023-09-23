def main():
    no = int(input('Enter a length of a list : '))
    elements = list()
    for i in range(no):
        elements.append(int(input('Enter element : ')))
    
    print(elements)

    filterdList = list(filter(lambda no: (no >= 70 and no <= 90), elements))
    print(filterdList)

if (__name__ == '__main__'):
    main()

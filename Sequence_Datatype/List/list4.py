def main():
    length = int(input('Enter number of elements that you want to store : '))
    Arr = list()
    for i in range(length):
        print('Enter', i ,'th element : ', end='')
        Arr.append(input())

    print('--------------------------------------')
    print('\nPrint list with for loop')
    for i in range(length):
        print(Arr[i], end=' ')

    print('\n\nPrint whole list')
    print(Arr)

if (__name__ == '__main__'):
    main()

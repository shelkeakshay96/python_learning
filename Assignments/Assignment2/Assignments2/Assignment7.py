def main():
    print('Star pattern -----')
    no1 = int(input('Enter length of j : '))

    for i in range(no1):
        for j in range(1, no1+1):
            print(j, end=' ')
        print()

if (__name__ == '__main__'):
    main()
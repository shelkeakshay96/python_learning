def main():
    print('Star pattern -----')
    no1 = int(input('Enter length of * : '))

    for i in range(no1):
        for j in range(i, no1):
            print('*', end=' ')
        print()

if (__name__ == '__main__'):
    main()
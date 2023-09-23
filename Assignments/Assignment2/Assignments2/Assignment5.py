def main():
    print('---Prime---')
        
    no = int(input('Enter a number '))
    i = 2
    isFactors = False

    while(i < no):
        if (no % i == 0):
            isFactors = True
            break
        i = i + 1

    if (isFactors ==  False):
        print(no, 'is a prime number')
    else:
        print(no, 'is a not a prime number')

if (__name__ == '__main__'):
    main()
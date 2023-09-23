def main():
    print('---Factorial---')
    no = int(input('Enter a positive number : '))
    factorial = 1;
    i = no

    while (i > 0):
        factorial = factorial * i
        i = i - 1

    print('Factorial of' ,no, 'is :', factorial)

if (__name__ == '__main__'):
    main()

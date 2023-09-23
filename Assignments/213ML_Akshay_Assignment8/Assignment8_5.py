def factorialRec(no, factorial = 1):
    if (no < 1):
        return factorial

    factorial = factorial * no
    no = no - 1

    return factorialRec(no, factorial)

def main():
    print('Find Factorial of number using recursive function')
    inputNumber = int(input('Enter a number : '))
    print('Factorial of number {} is : {}'. format(inputNumber, factorialRec(inputNumber)))

if (__name__ == '__main__'):
    main()

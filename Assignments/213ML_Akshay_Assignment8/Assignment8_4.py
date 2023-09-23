def sumDigits(no):
    sum = 0
    while (no >= 1):
        lastDigit = int(no % 10)
        sum = sum + lastDigit
        no = no / 10
        print(no)
    return sum

def sumDigitsR(no, sum = 0):
    if (no < 1):
        return sum
    
    lastDigit = int(no % 10)
    sum = sum + lastDigit
    no = no / 10

    return sumDigitsR(no, sum)

def main():
    print('Print a pattern using recursive function')
    inputNumber = int(input('Enter a number : '))
    print('Sum of digits in number {} is : {}'. format(inputNumber, sumDigitsR(inputNumber)))

if (__name__ == '__main__'):
    main()

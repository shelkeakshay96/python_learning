import Module.Arithmetic as math

def main():
    print('Enter 2 numbers');
    no1 = int(input('Enter first number : '))
    while (True):
        no2 = int(input('Enter second number : '))
        if (no2 == 0):
            print('Second number cannot be 0 (Zero). Please enter another number again')
        else:
            break;

    print('Addition is :' , math.Add(no1, no2))
    print('Substraction is :' , math.Sub(no1, no2))
    print('Multiplication is :' , math.Mult(no1, no2))
    
    
    print('Division is :' , math.Div(no1, no2))

if (__name__ == '__main__'):
    main()

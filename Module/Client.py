def main():
    Value1 = int(input('Enter fisrt number : '))
    Value2 = int(input('Enter second number : '))
    Result = 0
    Result = Maths.Addition(Value1, Value2)
    print('Addition is :',Result)

    Result = Maths.Substraction(Value1, Value2)
    print('Substraction is :',Result)

    Result = Maths.Multiplication(Value1, Value2)
    print('Multiplication is :',Result)

    Result = Maths.Division(Value1, Value2)
    print('Division is :',Result)

def DisplayModule2():
    print('Special variable of Client.py is : ', __name__)

if (__name__ == '__main__'):
    main()
import sys

def main():
    Value1 = int(sys.argv[1])
    print('First number is ', Value1)
    Value2 = int(sys.argv[2])
    print('\nSecond number is ', Value2)
    Addition = Value1 + Value2

    print('\nAddition is :', Value1 , '+', Value2, '=', Addition)

if (__name__ == '__main__'):
    main()
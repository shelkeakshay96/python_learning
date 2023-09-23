
def printPattern(no, i = 1):
    if (i > no ) :
        print()
        return

    print (i, end=' ')
    i = i + 1
    printPattern(no, i)
    

def main():
    print('Print a pattern using recursive function')
    inputNumber = int(input('Enter a number : '))
    printPattern(inputNumber)

if (__name__ == '__main__'):
    main()

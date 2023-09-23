def main():
    print('---Factors---')
        
    no = int(input('Enter a number '))
    i = 1
    additionOfFactors = 0
    while(i <= no):
        if (no % i == 0):
            print (i)
            additionOfFactors = additionOfFactors + i
        i = i + 1

    print('Addition Of Factors is :', additionOfFactors)

if (__name__ == '__main__'):
    main()
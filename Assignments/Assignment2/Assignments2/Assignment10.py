def main():
    print('-----Addition of a Digit-----')
    no = int(input('Enter a number : '))

    addition = 0
    while (True):
        if (no >= 1):
            addition = addition + (no % 10)
            no = int(no / 10)
        else:
            break;

    print('Addition of a digit :', addition)

if (__name__ == '__main__'):
    main()
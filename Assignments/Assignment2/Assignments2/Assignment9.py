def main():
    print('-----Digit of a number-----')
    no = int(input('Enter a number : '))

    count = 0
    while (True):
        if (no >= 1):
            count = count + 1
            no = int(no / 10)
        else:
            break;

    print (count)

if (__name__ == '__main__'):
    main()
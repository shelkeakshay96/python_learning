def main():
    print('Enter 2 numbers')
    value1 = int(input())
    value2 = int(input())
    multi = lambda no1, no2: no1 * no2
    ans = multi(value1, value2)
    print('{} X {} = {}'. format(value1, value2, ans))

if (__name__ == '__main__'):
    main()

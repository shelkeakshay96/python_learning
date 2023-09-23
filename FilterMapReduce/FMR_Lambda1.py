from functools import reduce

def main():
    data = list()
    no = int(input('Enter length of list elements : '))
    for i in range(no):
        data.append(int(input('Enter list element : ')))

    print('list is :', data)

    output = list(filter(lambda no: (no % 2 == 0), data))
    print('filter even numbers are {}' . format(output))

    moutput = list(map(lambda no: no + 2, output))
    print('map add 2 in numbers {}'.format(moutput))

    result = reduce(lambda no1, no2: (no1 + no2), moutput)
    print(result)

if (__name__ == '__main__'):
    main()

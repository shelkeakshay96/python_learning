import sys
j = 0
def displayF(i):
    if (i > 0):
        print(i)
        displayF(i-1)

def displayW(i):
    while (i < 5):
        print(i)
        i = i + 1

def main():
    print('limit :' , sys.getrecursionlimit())
    no = 5
    displayF(no)
    displayW(0)


if (__name__ == '__main__'):
    main()
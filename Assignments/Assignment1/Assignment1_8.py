# Write a function that prints * no of times as input numner
def printStar(No):
    for i in range(No):
        print('*', end=' ')
    print()

def main():
    No = int(input('Enter a number : '))
    printStar(No)

if (__name__ == "__main__"):
    main()

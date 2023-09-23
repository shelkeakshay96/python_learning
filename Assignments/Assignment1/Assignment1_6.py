# Write a function that gives positive or negative or zero
def checkNumber(No):
    if (No > 0):
        print('Positive')
    elif (No < 0):
        print('Negative')
    else:
        print('Zero')

def main():
    No = float(input('Enter a number : '))
    checkNumber(No)

if (__name__ == "__main__"):
    main()

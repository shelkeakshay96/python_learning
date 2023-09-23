# Write a function that checkes if number is divisible by 5
def checkNoDivisibleBy5(No):
    if (No % 5 == 0):
        return True
    else:
        return False

def main():
    No = float(input('Enter a number : '))
    print(checkNoDivisibleBy5(No))

if (__name__ == "__main__"):
    main()

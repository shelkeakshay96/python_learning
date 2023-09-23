# Write a function that gives addition of 2 number
def add(No1, No2):
    return No1 + No2

def main():
    No1 = int(input('Enter First number : '))
    No2 = int(input('Enter Second number : '))
    print(add(No1, No2))

if (__name__ == "__main__"):
    main()

# Write a function that prints length of a string
def getStringLength(str):
    count = 0
    for i in str:
        count = count + 1
    return count

def main():
    str = input('Enter a String : ')
    print(getStringLength(str))

if (__name__ == "__main__"):
    main()

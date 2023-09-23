
def Addition(no1, no2):
    return no1 + no2

def main():
    value1 = int(input('Enter First Number : '))
    value2 = float(input('Enter Second Number : '))
    answer = 0
    answer = Addition(value1, value2)
    print("Addition is :",answer)

#__name__ is a special variable
# gives output it runs with which module
if (__name__ == "__main__"):
    main()

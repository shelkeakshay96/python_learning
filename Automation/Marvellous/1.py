# Function defines another function inside it and returns its return value
def sum1():
    def add(a, b):
        return a + b

    return add

def sum2(no1, no2):
    def add(a, b):
        return a + b
    
    return add(no1, no2)

def main():
    value1 = 10
    value2 = 20
    ret = sum1()
    ans = ret(value1, value2)
    print('Addition is :', ans)
    print('Addition is :', sum2(value1, value2))
    
if (__name__ == '__main__'):
    main()

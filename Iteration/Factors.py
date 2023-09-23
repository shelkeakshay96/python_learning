# Demonstation of Factors

def getFactors(No):
    factors = []
    for i in range(1, No + 1):
        if(No % i == 0):
            factors.append(i)
    return factors

def getFactorsByWhlie(No):
    factors = []
    i = 1
    while (No+1 > i):
        if (No % i == 0):
            factors.append(i)
        i = i + 1
    return factors

def main():
    No = int(input('Enter Number : '))
    # print(getFactors(No))
    print(getFactorsByWhlie(No))

if(__name__ == '__main__'):
    main()

import ModuleNumbers

class Numbers:
    def __init__(self) -> None:
        self.value = 0

    def chkPrime(self):
        isPrime = True
        for i in range(2, self.value):
            if (self.value % i == 0):
                isPrime = False

        return isPrime
    
    def chkPerfect(self):
        sum = 0
        for i in range (1, self.value):
            if (self.value % i == 0):
                sum = sum + i

        if (sum == self.value):
            return True
        else:
            return False
    
    def sumFactors(self):
        sumFactors = 0
        i = 1
        while (i <= self.value):
            if (self.value % i == 0):
                sumFactors = sumFactors + i
            i = i + 1

        return sumFactors

    def factors(self):
        listFactors = []
        i = 1
        while (i <= self.value):
            if (self.value % i == 0):
                listFactors.append(i)
            i = i + 1

        return listFactors

    def accept(self):
        self.value = int(input('Enter a number : '))

def main():
    print('---Numbers---')

    num1 = Numbers()
    num1.accept()

    print('Check prime : ', num1.chkPrime())
    print('Check Perfect : ', num1.chkPerfect())
    print('Sum of Factors : ', ModuleNumbers.sumFactors(num1.value))
    print('List of Factors : ', num1.factors())

if (__name__ == '__main__'):
    main()

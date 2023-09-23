class Arithmetic:
    def __init__(self) -> None:
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        self.value1 = int(input('Enter first number : '))
        self.value2 = int(input('Enter second number : '))
    
    def addition(self):
        return self.value1 + self.value2
    
    def substraction(self):
        return self.value1 - self.value2
    
    def multiplication(self):
        return self.value1 * self.value2
    
    def division(self):
        return self.value1 / self.value2

def main():
    obj1 = Arithmetic()
    obj1.accept()
    print('addition :', obj1.addition())
    print('substraction :', obj1.substraction())
    print('multiplication :', obj1.multiplication())
    print('division :', obj1.division())


    obj2 = Arithmetic()
    obj2.accept()
    print('addition :', obj2.addition())
    print('substraction :', obj2.substraction())
    print('multiplication :', obj2.multiplication())
    print('division :', obj2.division())

if (__name__ == '__main__'):
    main()

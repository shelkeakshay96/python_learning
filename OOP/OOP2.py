class Demo:
    def __init__(self, Value1, Value2) -> None:                     # Constructior
        print('inside init constructor')
        self.No1 = Value1
        self.No2 = Value2

    def display(self):
        print('Value of No1 {}'. format(self.No1))
        print('Value of No2 {}'. format(self.No2))

def main():
    print('Demonstration of Object Orientation')

    obj1 = Demo(10, 20)
    obj2 = Demo(11, 21)

    obj1.display()
    obj2.display()

if (__name__ == '__main__'):
    main()

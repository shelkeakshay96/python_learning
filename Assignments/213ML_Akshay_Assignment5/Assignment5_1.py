class Demo:
    Value = 100
    def __init__(self, i, j) -> None:
        self.no1 = i
        self.no2 = j

    def fun(self):
        print('fun : {}, {}'. format(self.no1, self.no2))

    def gun(self):
        print('gun : {}, {}'. format(self.no1, self.no2))

def main():
    print('Demo class')
    obj1 = Demo(10, 20)
    obj2 = Demo(11, 21)

    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()

    print(Demo.Value)

if (__name__ == '__main__'):
    main()

print('---Demonstration of Class in python---')

class Demo:
    def __init__(self):
        self.i = 0
        self.j = 0

    def fun(self):                              # Instance method
        print('inside fun {}'.format(self.i))   # We can use 

    @classmethod
    def gun(obj):                               # class object is must to pass in classmethods
        print('inside class method')
        print('from gun : ', end='')         
        obj.sun()                               # Class method can call its static methods

    @staticmethod
    def sun():
        print('inside sun')
        print('from sun : ', end='')         

obj1 = Demo()
obj1.fun()
Demo.fun(obj1)
obj1.gun()
Demo.gun()
obj1.sun()
Demo.sun()


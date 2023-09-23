class Circle:
    PI = 3.14

    def __init__(self) -> None:
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self):
        self.radius = float(input('Enter radius : '));

    def calculateArea(self):
        self.area = format(Circle.PI * (self.radius * self.radius), ".2f")

    def calculateCircumference(self):
        self.circumference = format(2 * Circle.PI * self.radius, ".2f")

    def display(self):
        print('Radius of circle : {} '. format(self.radius))
        print('Area of circle: {} '. format(self.area))
        print('Circumference of circle: {} '. format(self.circumference))

def main():
    circle1 = Circle()
    circle2 = Circle()
    circle3 = Circle()

    circle1.accept()
    circle1.calculateArea()
    circle1.calculateCircumference()
    circle1.display()
    
    circle2.accept()
    circle2.calculateArea()
    circle2.calculateCircumference()
    circle2.display()
    
    circle3.accept()
    circle3.calculateArea()
    circle3.calculateCircumference()
    circle3.display()

if (__name__ == '__main__'):
    main()

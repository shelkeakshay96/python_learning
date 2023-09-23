def DisplayMultiple(*Companies):
    print(Companies)

def Display(Name, Age=27, *Companies):
    print('Name : ', Name)
    print('Age : ', Age)
    print('Companies : ', Companies)

def main():
    Display('Akshay')                       # Default Arguments
    Display('Rutuja', 26)                   # Positinal arguments
    Display(Age=26, Name='Rutuja')          # Keyword Argument
    DisplayMultiple('Hotspot', 'Panacea')   # Variable Number of Arguments
    Display('Akshay', 28, 'Hotspot', 'Panacea', 'Katalyst', 'Seniority', 'Encora')         # Variable Number of Arguments

if (__name__ == '__main__'):
    main()

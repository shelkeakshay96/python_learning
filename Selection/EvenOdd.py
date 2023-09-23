# import Module.Maths as Maths
# SELECTION : 
# import Module.Maths as Maths
# Maths.path.append('../Module')pw

def IsEven(No):
    if (No % 2 == 0):
        Answer = 'Even'
    else:
        Answer = 'Odd'
    return Answer

def main():
    No = int(input('Enter a Number : '))
    print(No ,'is a',IsEven(No),'number')

if (__name__ == '__main__'):
    main()

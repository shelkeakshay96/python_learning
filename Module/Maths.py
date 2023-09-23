def Addition(No1, No2):
    Answer = 0
    Answer = No1 + No2
    return Answer

def Substraction(No1, No2):
    Answer = 0
    Answer = No1 - No2
    return Answer

def Multiplication(No1, No2):
    Answer = 0
    Answer = No1 * No2
    return Answer

def Division(No1, No2):
    Answer = 0
    Answer = No1 / No2
    return Answer

def IsEven(No):
    if (No % 2 == 0):
        Answer = 'Even'
    else:
        Answer = 'Odd'
    return Answer

def getFactors(No):
    my_list = []
    for i in range(1, No + 1):
        if(No % i == 0):
            my_list.append(i)
    
    return my_list

def DisplayModule1():
    print('Special variable of Maths.py is : ', __name__)

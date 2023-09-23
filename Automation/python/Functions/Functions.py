
# Fuctions accepts nothing and return nothing
def marvellous():
    print('Hello world')
    # pass

# functions accets one paramer as name and retrns nothing
def marvellousName(name):
    print('Welcome to python {}'. format(name))

# functions accets multiple paramers as name, age, city and retrns nothing
def marvellousParams(name, age, city):
    print('Welcom :', name)
    print('Your age is :', age)
    print('Your city is :', city)

# functions accets multiple paramers as return one parameter
def getMaxNumber(no1, no2):
    if (no1 > no2):
        return no1
    else:
        return no2
    
# functions accets multiple paramers as return multiple parameters
def arrithmetic(no1, no2):
    addition = no1 + no2
    substracion = no1 - no2
    multiplication = no1 * no2
    division = no1 / no2

    return addition, substracion, multiplication, division

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def addSub(value1, value2):
    addParam = add(value1, value2)
    print('addition of nested function is ', addParam)

    subParam = sub(value1, value2)
    print('substration of nested function is ', subParam)

    return addParam, subParam

# Function name as parameter
def parameterAsFunction(FPTR):
    print('type of param FPTR :', type(FPTR))
    print(FPTR)
    Ans = FPTR(11, 2)
    print('Additoin is :', Ans)

# Function inside 
def innerFunction(no1, no2):
    def addInner(a, b):
        return a + b

    ans = addInner(no1, no2)
    return ans

def main():
    marvellous()
    marvellousName('Akshay')
    print('----------------------')
    marvellousParams('Akshay', 28, 'Satara')
    print('----------------------')
    marvellousParams(age=28, name='Akshay', city='Satara')  # parameters sequence can change with param name
    print('----------------------')
    value1 = 10
    value2 = 20
    max = getMaxNumber(value1, value2)
    print('Max number between {} and {} is : {}'. format(value1, value2, max))
    print('----------------------')

    addParam, sub, mult, div = arrithmetic(value1, value2)   # accpt multiple return values
    print('addition : ' , addParam)
    print('substracion : ' , sub)
    print('multiplication : ' , mult)
    print('division : ' , div)
    print('----------------------')
    
    ret = arrithmetic(value1, value2)   # accpt multiple return values in list
    print('addition : ' , ret[0])
    print('substracion : ' , ret[1])
    print('multiplication : ' , ret[2])
    print('division : ' , ret[3])
    print('----------------------')

    addSubParam = addSub(value1, value2)
    print('addition is : ',addSubParam[0])
    print('sustraction is :', addSubParam[1])
    print('----------------------')

    addLambda = lambda no1, no2: no1 + no2
    print('additio using lamda :', addLambda(value1, value2))
    
    print('----------------------')
    subLambda = lambda no1, no2: no1 - no2
    print('substraction using lamda :', subLambda(value1, value2))

    print('----------------------')
    print('addntion using functio name as param:')
    parameterAsFunction(add)
    print('----------------------')

    print('additoin of inner function :', innerFunction(value1, value2))

    print('----------------------')
if (__name__ == '__main__'):
    main()

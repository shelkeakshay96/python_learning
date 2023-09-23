def main():
    while (True):
        try:
            no1 = int(input('Enter first number : '))
            no2 = int(input('Enter second number : '))
            break
        except ValueError as e:
            print('Input should be number.', e)
        finally:
            ans = 0

    try:
        ans = no1 / no2
    except ZeroDivisionError as e:
        print('Cannot devide by zero', e)
        return
    finally:
        print('In finally block: It will execute always')

    print('Divisio :', ans)

if (__name__ == '__main__'):
    try:
        main()
    except KeyboardInterrupt as e:
        print('Exiting the program...', e)
    except Exception as e:
        print('Terminating the program', e)

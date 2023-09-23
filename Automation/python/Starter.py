import Module.Maths as module_maths
import Module.Client as module_client

def main():
    print('Special variable of Starter.py is : ', __name__)

    module_maths.DisplayModule1()
    module_client.DisplayModule2()

if (__name__ == '__main__'):
    main()
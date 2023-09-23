import sys

def main():
    print('Demonstation of Command line arguments')
    print('Number of command line arguments are : ', len(sys.argv))
    print('Command line arguments are : ', sys.argv)


    print(sys.argv[0])
    for i in range(len(sys.argv)):
        print(sys.argv[i])

if (__name__ == '__main__'):
    main()
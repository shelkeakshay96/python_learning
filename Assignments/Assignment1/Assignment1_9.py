# Write a function that prints first 10 even numbers
def print10EvenNo():
    No = 0
    i = 1
    while (No < 10):
        if (i % 2 == 0):
            print(i, end='  ')
            No = No + 1
        i = i + 1
    print()

def main():
    print10EvenNo()

if (__name__ == "__main__"):
    main()

import time

def square(n):
    return (n * n)

def main():
    arr = [1, 2, 3, 4, 5]
    print(arr)
    result = []
    start = time.time()
    for i in arr:
        result.append(square(i))
    end = time.time()
    
    print(result)
    print((end-start) * 10**3, "ms")

if (__name__ == '__main__'):
    main()

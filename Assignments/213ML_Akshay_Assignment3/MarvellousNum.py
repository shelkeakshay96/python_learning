def chkPrime(no):
    isPrime = True
    for i in range(2, no):
        if (no % i == 0):
            isPrime = False
            break
    
    return isPrime
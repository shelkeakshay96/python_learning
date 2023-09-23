def sumFactors(no):
    sumFactors = 0
    i = 1
    while (i <= no):
        if (no % i == 0):
            sumFactors = sumFactors + i
        i = i + 1

    return sumFactors

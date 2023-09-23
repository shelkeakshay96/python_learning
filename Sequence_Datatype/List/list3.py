data = [11, 'Marvellous', 3.14, True]

print('\n---sequence :---')
print(data[0], end=' ')
print(data[1], end=' ')
print(data[2], end=' ')
print(data[3])

print('\n---sequence reverce:---')
print(data[-1], end=' ')
print(data[-2], end=' ')
print(data[-3], end=' ')
print(data[-4])

print('\n---iteration for loop:---')
for i in range(len(data)):
    print(data[i], end=' ')
print('\n\n---iteration for loop with range all params:---')
for i in range(0, len(data), 1):
    print(data[i], end=' ')

print('\n\n---iteration while loop:---')
i = 0
while (i < len(data)):
    print(data[i], end=' ')
    i = i + 1
print('\n')
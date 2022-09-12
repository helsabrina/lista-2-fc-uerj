
arr = []
numPares = 0

for i in range(0, 41):
    arr.append(i)


for n in arr:
    if(n % 2 == 0):
        numPares += 1
        

print('A quantidade de elementos pares é:', numPares)

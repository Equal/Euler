#max number is when adding a 9 to the number increases it by greater than 9^5, so ~99,999
#tried that, but it was wrong, so increased the limit to 500k just to be safe

def sumOfFifthPower(i):
    i = str(i)
    localsum = 0
    for k in range(len(i)):
        localsum += pow(int(i[k]), 5)
    return localsum

totalsum = 0

for i in range(2, 500000):
    if (sumOfFifthPower(i) == i):
        totalsum += i

print totalsum

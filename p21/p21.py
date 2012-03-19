def d(n):
    count = n - 1
    divisorsum = 0
    while (count > 0):
        if (n % count == 0):
            divisorsum += count
        count -= 1
    return divisorsum


a = 1
dofa = 0
totalsum = 0

while (a < 10000):
    dofa = d(a)
    if (d(dofa) == a):
        if (dofa > a):
            print a
            print dofa
            totalsum += a
            totalsum += dofa
    a += 1

print totalsum

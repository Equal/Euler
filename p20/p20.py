import math

crazynum = long(math.factorial(100))
digitsum = 0

while crazynum:
    lastdigit = crazynum % 10
    digitsum += lastdigit
    crazynum = (crazynum - lastdigit) / 10

print digitsum

#I learned that python rounding errors are prevalent in numbers this big. Had to use long explicitly instead of letting python automatically use floats, which gave me the wrong result.


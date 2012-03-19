s = 0

for x in xrange(1, 1001):
    s += pow(x, x)
    print s

print s % 100

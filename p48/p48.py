crazysum = 0

for i in range(1, 1000):
    crazysum += pow(i, i)

goodnum = crazysum % 10000000000

print goodnum

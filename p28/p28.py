#noticed a pattern in the series of the diagonals of the spiral - abusing that

diagsum = 1
count = 1
for i in range(2, 1002, 2):
    for k in range(4):
        count += i
        print count
        diagsum += count

print diagsum

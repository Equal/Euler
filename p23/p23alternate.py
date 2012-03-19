#According to wikipedia, every integer greater than 20161 can be written as abundant sums
def isAbundantNumber(number):
    sqrtnum = int(number**0.5) + 1
    divisorsum = 1 #already account for 1
    for i in range(2, sqrtnum):
        if number % i == 0:
            divisorsum += i
            if (number / i != i):
                divisorsum += number / i
    if (divisorsum > number):
        return True
    return False

#Options: Find all abundant numbers, store in array sorted, then check those for sum
#Options: Brute force
#Solution: Brute force - because I don't know how many abundant numbers there are before 20161, and the space costs might offset the performance gains

abundantnumbers = []
abundantSums = set()
answer = 0
for i in range(12, 20162):
    if (isAbundantNumber(i)):
        abundantnumbers.append(i)

print len(abundantnumbers)

for i in abundantnumbers:
    for k in abundantnumbers:
        if i + k < 20162:
            abundantSums.add(i+k)

print sum([x for x in range(20162) if x not in abundantSums])

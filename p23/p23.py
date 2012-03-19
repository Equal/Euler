#According to wikipedia, every integer greater than 20161 can be written as abundant sums
def isAbundantNumber(number):
    divisorsum = 0
    for i in range(1, number):
        if number % i == 0:
            divisorsum += i
    if (divisorsum > number):
        return True
    return False

#Options: Find all abundant numbers, store in array sorted, then check those for sum
#Options: Brute force
#Solution: Brute force - because I don't know how many abundant numbers there are before 20161, and the space costs might offset the performance gains

abundantnumbers = []
abundantSums = {}
answer = 0
for i in range(12, 20162):
    if (isAbundantNumber(i)):
        abundantnumbers.append(i)

print len(abundantnumbers)

for i in range(len(abundantnumbers)):
    for k in range(i, len(abundantnumbers)):
        abundantSums[abundantnumbers[i]+abundantnumbers[k]] = 1

print len(abundantSums)

for i in range(1, 20162):
    if abundantSums.get(i, None) == None: 
        answer += i

print answer

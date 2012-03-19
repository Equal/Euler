#A parser to grab data
import sys, string

problemArray = []

problemFile = open('input.txt', 'r')

for line in problemFile.readlines():
    if line[0] == '':
        break
    
    row = []

    for character in line:
        if character.isdigit():
            number = int(character)
            row.append(number)

    problemArray.append(row)

#define some helpful functions
def sumColumn(colnum):
    sum = 0
    for row in problemArray:
        sum += row[colnum]
    return sum

def getLeadingDigits(num):
    num = (num - (num % 10)) / 10
    return num

#time to do the calculations
answerArray = []
colnum = len(problemArray[0]) - 1 #Yes, I know - this assumes the array will be filled with numbers of equal length
lastoverflow = 0

while colnum > 0:
    sum = sumColumn(colnum) + lastoverflow
    lastoverflow = getLeadingDigits(sum)

    if colnum < 10:
        answerArray.insert(0, sum % 10)
    colnum -= 1

#now for the last column
sum = sumColumn(0)
sum += lastoverflow
print sum
print answerArray


#Things I learned: I have a tendency to forget little details

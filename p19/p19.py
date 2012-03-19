import math

def getFirstSundaysInYear(startValue, isLeap):
    count = 0

    for monthNum in range(1, 13):
        if (startValue % 7 == 0):
            count += 1
        if (monthNum in [4, 6, 9, 11]):
            startValue += 30
        elif (monthNum == 2):
            if (isLeap):
                startValue += 29
            else:
                startValue += 28
        else:
            startValue += 31

    return count

yearStart = 2 #because jan 1, 1901 is a tuesaday
totalCount = 0
year = 1901

while (year <= 2000):
    isLeap = (year % 4 == 0) and (year % 100 != 0)
    totalCount += getFirstSundaysInYear(yearStart, isLeap) 
    if (isLeap):
        yearStart += 366
    else:
        yearStart += 365
    year += 1

print totalCount

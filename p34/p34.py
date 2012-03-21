"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

#9! is 362880, so a max search value of one million sounds like a good first guess. If I can lower this limit at a later time, I will. Adding a digit will not increase the sum by amount that the number itself will increase by
#I think maybe a lookup will be slower than calculating the factorial every single time, so I'll try that

from math import factorial

factorials = []
curiousNumbers = []
max_limit = 1000000
localsum = 0

for i in range(0, 10):
    factorials.append(factorial(i))

for i in range(3, max_limit):
    localsum = 0
    for k in str(i):
        localsum += factorials[int(k)]
        if (localsum > i):
            break
    if (i == localsum):
        curiousNumbers.append(i)
        print i

localsum = 0

print sum(curiousNumbers)


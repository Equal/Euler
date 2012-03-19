#Brute Force

def sequence(num):
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        steps += 1
    return steps

longestChain = 0
longestChainNumber = 0

curnum = 999999

while curnum > 1:
    steps = sequence(curnum)
    if steps > longestChain:
        longestChain = steps
        longestChainNumber = curnum
    curnum -= 1

print longestChainNumber
print longestChain


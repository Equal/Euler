"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

answer = 0
def isPalindrome(num):
    num = str(num)
    revnum = num[::-1] #neat trick to reverse a string
    if (num == revnum):
        return True
    return False

for i in range(1000000):
    if (isPalindrome(i)):
        if (isPalindrome(bin(i)[2:])):
            answer += i

print answer


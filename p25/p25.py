term = 2 #2 because it's the second term that reaches 1000
m = 1
n = 1

while (len(str(n)) < 1000):
    n = n + m
    m = n - m
    term += 1

print term

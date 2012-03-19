import sys, string

triangle = []

f = open('triangle.txt', 'r')

for line in f.readlines():
    if line[0] == '':
        break

    row = list(map(int, string.split(line)))
    triangle.append(row)

#now we've got the triangle. let's kick some ass.
#bottom up is obviously the way to go. let's do this in o(n) time!

for row in range(len(triangle)-2, -1, -1):
    for col in range(0, len(triangle[row])):
        triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])

print triangle[0][0]
    



    



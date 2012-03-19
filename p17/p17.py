singledigits = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
}

firsttens = {
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen'
}

othertens = {
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'
}

answer = ''

for i in range(1, 1000):

    #first check for special exception of first tens
    lasttwo = i % 100
    if lasttwo >= 10 and lasttwo <=19:
        answer = firsttens[lasttwo] + answer
    else:
        lastdigit = lasttwo % 10
        if lastdigit > 0:
            answer = singledigits[lastdigit] + answer
        lasttwo = lasttwo - lastdigit
        if (lasttwo > 0):
            answer = othertens[lasttwo] + answer

    lasttwo = i % 100
    hundredth = (i - lasttwo) / 100
    if (hundredth > 0):
        if lasttwo > 0:
            answer = singledigits[hundredth] + 'hundredand' + answer
        else:
            answer = singledigits[hundredth] + 'hundred' + answer

answer = 'onethousand' + answer
print answer
print len(answer)



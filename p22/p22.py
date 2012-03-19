import sys, string

def getAlphabetPosition(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet.find(letter) + 1

def getWordValue(word):
    value = 0
    for i in range(len(word)):
        value += getAlphabetPosition(word[i])
    return value

namesFile = open('names.txt', 'r')
names = []

for line in namesFile.readlines():
    for name in line.split(','):
        name = string.replace(name, '"', '')
        names.append(name)

names.sort()

nameScores = [getWordValue(names[i]) * (i+1) for i in range(len(names))]
totalScore = 0

for score in nameScores:
    totalScore += score
print totalScore

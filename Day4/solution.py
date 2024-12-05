import time
def getDiagonals(textArray):
    diagonalList = []
    for i in range(len(textArray)):
        word1 = ""
        word2 = ""
        for x, y in zip(range(i, -1, -1), range(0, i+1, 1)):
            word1+=textArray[y][x]
        for x, y in zip(range(i + 1, len(textArray[0]), 1), range(len(textArray[0]) - 1, i + 1 - 1, -1)):
            word2+=textArray[y][x]
        diagonalList.extend([word1, word2])
        word1 = ""
        word2 = ""
    return diagonalList

def flipArray(textArray):
    flipped = []
    for text in textArray:
        flipped.append(text[::-1])
    return flipped

def getVerticalLines(textArray):
    verticalLines = []
    for i in range(len(textArray[0])):
        vert = ""
        for y in range(len(textArray)):
            vert += textArray[y][i]
        verticalLines.append(vert)
        vert = ""
    return verticalLines

input = open("input.txt", "r").read().split("\n")

def part1(input, word, fA=False):
    allLines = []
    if(fA):
        allLines.extend([getDiagonals(input), getDiagonals(flipArray(input))])
    else:
        allLines.extend([getDiagonals(input), getDiagonals(flipArray(input)), getVerticalLines(input), input])
    count = 0
    for lineArray in allLines:
        for line in lineArray:
            count += line.count(word) + line[::-1].count(word)

    return count

def part2():
    count = 0
    possibilities = []
    for y in range(1, len(input) - 1):
        line = input[y]
        for x in range(len(line)):
            if(line[x] == "A" and x > 0 and x < len(line) - 1):
                i = ([input[y - 1][x-1:x+2], input[y][x-1:x+2], input[y + 1][x-1:x+2]])
                temp_count = part1(i, "MAS", True)
                if(temp_count == 2):
                    count += 1
                temp_count = 0
    return count

part1(input, "XMAS")
print(part2())

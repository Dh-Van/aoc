import re
input = open("../input.txt", "r").read()

def part1():
    print(sum([int(t[0]) * int(t[1]) for t in re.findall("mul\((\d+),(\d+)\)", input)]))

def part2():
    keywords = re.findall("(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)", input)
    do_sum = True
    sum = 0
    for keyword in keywords:
        if(keyword[0]): do_sum = False
        elif(keyword[1]): do_sum = True
        elif(do_sum):
            sum += int(keyword[2]) * int(keyword[3])
    print(sum)

part1()    
part2()

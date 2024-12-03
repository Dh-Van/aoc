import re

input = open("input.txt", "r").read()

def part1():
    y = re.findall("mul\([\d]{1,3},[\d]{1,3}\)", input)
    sum = 0
    for s in y:
        numbers = re.split("\(|\)", s)
        nums = [int(n) for n in re.split(",", numbers[1])]
        print(nums)
        sum += nums[0] * nums[1]


    print(sum)

def part2():
    y = re.findall("don\'t\(\)|do\(\)|mul\([\d]{1,3},[\d]{1,3}\)", input)
    sum = 0
    sum_flag = True
    for s in y:
        if(s == "don\'t()"): 
            sum_flag = False
            continue
        if(s == "do()"): 
            sum_flag = True
            continue
        print(s, sum_flag)
        if(sum_flag):
            numbers = re.split("\(|\)", s)
            nums = [int(n) for n in re.split(",", numbers[1])]
            sum += nums[0] * nums[1]
    print(sum)



part2()
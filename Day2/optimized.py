input = [list(map(int, line.split())) for line in open("input.txt", "r").read().split("\n")]

def part1():
    passed_levels = 0
    for level in input:
        sorted_level_inc = sorted(level)
        sorted_level_dec = sorted(level, reverse=True)
        if(sorted_level_inc != level and sorted_level_dec != level): continue

        diff_list = []
        for i in range(2, len(level)):
            diff_list.append(abs(level[i - 1] - level[i]))

        if(all(num > 0 and num < 4 for num in diff_list)): 
            passed_levels += 1

    print(passed_levels)

def part2():
    passed_levels = 0
    for level in input:
        temp_count = 0
        for i in range(len(level) + 1):
            augmented_level = level[0:i] + level[i + 1:]
            sorted_level_inc = sorted(augmented_level)
            sorted_level_dec = sorted(augmented_level, reverse=True)
            if(sorted_level_inc != augmented_level and sorted_level_dec != augmented_level): continue

            diff_list = []
            for i in range(1, len(augmented_level)):
                diff_list.append(abs(augmented_level[i - 1] - augmented_level[i]))

            if(all(num > 0 and num < 4 for num in diff_list)): 
                temp_count += 1
        passed_levels += min(temp_count, 1)
    print(passed_levels)

part2()
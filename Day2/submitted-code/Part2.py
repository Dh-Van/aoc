input = open("input.txt", "r")

input_list = [] 
for i in input.readlines(): input_list.append(i.split("\n")[0])
count = 0
for i in input_list:
    print("x")
    nums_s = i.split(" ")
    nums = []
    for n in nums_s: nums.append(int(n))
    recount = 0
    for k in range(len(nums) + 1):
        if(k != 0):
            temp = nums.copy()
            temp.pop(k - 1)
        else:
            temp = nums.copy()

        diff_list = []
        for i, n in enumerate(temp):
            if(i >= len(temp) - 1): continue
            diff_list.append(temp[i + 1] - n)

        temp_count = 0
        if(diff_list[0] != 0):
            last_sign = diff_list[0] / abs(diff_list[0])
        current_sign = last_sign
        for i, d in enumerate(diff_list):
            last_sign = current_sign
            if(d != 0):
                current_sign = d / abs(d)
            else:
                continue

            if(abs(d) >= 1 and abs(d) <= 3):
                if(current_sign != last_sign): 
                    continue
                temp_count += 1
                continue
            else:
                break
            
        if(temp_count == len(diff_list)): 
            count += 1
            recount += 1
            if(recount > 1):
                count -= 1
                break

print(count)

    
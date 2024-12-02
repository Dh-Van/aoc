input = open("../input.txt", "r")

input_list = [] 
for i in input.readlines(): input_list.append(i.split("\n")[0])
count = 0
for i in input_list:
    print("x")
    nums_s = i.split(" ")
    nums = []
    for n in nums_s: nums.append(int(n))

    diff_list = []
    for i, n in enumerate(nums):
        if(i >= len(nums) - 1): break
        diff_list.append(nums[i + 1] - n)

    print(diff_list)
    temp_count = 0
    if(diff_list[0] != 0):
        last_sign = diff_list[0] / abs(diff_list[0])
    else:
        continue
    current_sign = last_sign
    for i, d in enumerate(diff_list):
        last_sign = current_sign
        if(d != 0):
            current_sign = d / abs(d)
        else:
            break

        print(last_sign, current_sign)

        if(abs(d) >= 1 and abs(d) <= 3):
            if(current_sign != last_sign): 
                break
            temp_count += 1
            continue
        else:
            break
        
    if(temp_count == len(diff_list)): 
        #(nums)
        count += 1
    

print(count)

    
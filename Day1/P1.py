input = open("input.txt", "r")

input_list = input.readlines()
list1 = []
list2 = []

for i in input_list:
    s_i = i.split(" ")
    list1.append(int(s_i[0]))
    temp = s_i[-1]
    if(temp.find("\n") > 0):
        list2.append(int(s_i[-1][:-1]))
    else:
        list2.append(int(s_i[-1]))

s_1 = list1.sort()
s_2 = list2.sort()
dist = 0

for i in range(len(list1)):
    dist += abs(list1[i] - list2[i])
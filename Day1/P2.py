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

list1.sort()
list2.sort()
similarity = 0

for i in range(len(list1)):
    similarity += list1[i] * list2.count(list1[i])

print(similarity)

for i in range(len(list2)):
    similarity += list2[i] * list1.count(list2[i])


print(similarity)
parts = open("input.txt", "r").read().split("\n\n")

rules = [r.split("|") for r in parts[0].split("\n")]
pages = parts[1].split("\n")

transposed = list(zip(*rules))
# pages = [pages[4]]
correct_orders = []
incorrect_orders = []
for order_str in pages:
    was_right = True
    order = list(map(int, order_str.split(",")))
    running_list = []
    for i, num in enumerate(order):
        indices = [g for g, x in enumerate(transposed[0]) if int(x) == num]
        banned_pages = []
        if(indices):
            banned_pages = list(map(int, [transposed[1][index] for index in indices]))

        for page in running_list:
            if(banned_pages.count(page) > 0): 
                if(was_right):
                    incorrect_orders.append(order)
                was_right=False    

        running_list.append(num)
    if(was_right):
        correct_orders.append(order)

sum = 0            
for correct in correct_orders:
    idx = len(correct) / 2
    sum += correct[int(idx)]

# print(incorrect_orders)
fixed = []
for incorrect in incorrect_orders:
    correct = []
    for i, num in enumerate(incorrect):
        indices = [g for g, x in enumerate(transposed[0]) if int(x) == num]

        banned_pages = []

        if(indices):
            banned_pages = list(map(int, [transposed[1][index] for index in indices]))

        for idx, page in enumerate(correct):
            for banned in banned_pages:
                if(banned == page):
                    correct[idx] = num
                    num = banned

        correct.append(num)
    fixed.append(correct)

sum = 0            
for correct in fixed:
    idx = len(correct) / 2
    sum += correct[int(idx)]

print(sum)
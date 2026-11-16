values  = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

items = []
for i in range(len(values)):
    ratio = values[i] / weights[i]
    items.append([ratio, values[i], weights[i]])
items.sort(reverse=True)
total = 0
for ratio, v, w in items:
    if capacity >= w:
        total += v             
        capacity -= w
    else:
        total += ratio * capacity   
        break

print("Maximum value =", total)
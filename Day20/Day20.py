import copy

original = []
ordered = []


with open("day20.txt") as day_file:
    line = day_file.readline().strip()
    index = 0
    while line:
        original.append((int(line) * 811589153, index))
        index += 1
        line = day_file.readline().strip()

ordered = copy.deepcopy(original)

for k in range(10):
    #for e in ordered:
    #    print(e[0], end=',')
    #print()
    for i in range(len(original)):

        o_value, o_index = original[i]

        if o_value == 0:
            continue
        
        actual_index, new_index = None, None

        for j in range(len(ordered)):
            if ordered[j][1] == o_index and ordered[j][0] == o_value:
                actual_index = j
                break

        if actual_index + o_value >= len(ordered) - 1:
            new_index = (actual_index + o_value) % (len(ordered) - 1)

        elif actual_index + o_value <= 0:
            new_index = (actual_index + o_value) % (len(ordered) - 1)
            if new_index < 0:
                new_index += len(ordered) - 1 

        else:
            new_index = actual_index + o_value
                
        ordered.pop(actual_index)
        ordered.insert(new_index, (o_value, o_index))

        #for e in ordered:
        #    print(e[0], end=',')
        #print()
        

res_sum = 0
zero_index = None
offsets = [1000, 2000, 3000]
for i in range(len(ordered)):
    if ordered[i][0] == 0:
        zero_index = i
        break

for o in offsets:
    index = (zero_index + o) % len(ordered)
    res_sum += ordered[index][0]

print(res_sum)

        


stacks = [[] for i in range(9)]

with open("stacks.txt") as s_file:
    line = s_file.readline()
    while line:
        for index in range(9):
            if line[index] != ' ':
                stacks[index].insert(0, line[index])
        line = s_file.readline()
      

with open("instructions.txt") as i_file:
    line = i_file.readline().strip()[5:].replace(' ', '')
    while line:
        from_split = line.split('from')
        to_split = from_split[1].split('to')

        count = int(from_split[0])
        fromm = int(to_split[0])
        too = int(to_split[1])

        #for _ in range(count): #part1
            #item = stacks[fromm-1].pop() #part1
            #stacks[too-1].append(item) #part1
        fromm = fromm-1
        too = too-1
        items = stacks[fromm][-count:]
        stacks[fromm] = stacks[fromm][:len(stacks[fromm]) - count]
        stacks[too] += items
        #print(stacks)
            
        line = i_file.readline().strip()[5:].replace(' ', '')

res = ''
for stack in stacks:
    res += stack[-1]
print(res)

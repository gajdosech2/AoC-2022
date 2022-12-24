import copy

rules = []
rules.append(["N", "NE", "NW", "N"])
rules.append(["S", "SE", "SW", "S"])
rules.append(["W", "NW", "SW", "W"])
rules.append(["E", "NE", "SE", "E"])

offsets = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1), "NE": (-1, 1), "NW": (-1, -1), "SE": (1, 1), "SW": (1, -1)}

ground = []
with open("day23.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        ground.append(list(line))
        line = day_file.readline().strip()


bigger = [['.' for col in range(len(ground[0]) + 200)] for row in range(len(ground) + 200)]
for i in range(len(ground)):
    for j in range(len(ground[0])):
        bigger[i+100][j+100] = ground[i][j]

for roundnum in range(1000):
    print(roundnum)
    backup = copy.deepcopy(bigger)
    #for row in bigger:
    #    for col in row:
    #        print(col, end='')
    #    print()
    
    elves = []
    for i in range(len(bigger)):
        for j in range(len(bigger[i])):
            if bigger[i][j] == '#':
                elves.append((i, j))

    proposals = []
    
    adjacency = {"N": False, "E": False, "S": False, "W": False, "NE": False, "NW": False, "SE": False, "SW": False}
    for elf in elves:
        flag = False
        a = copy.deepcopy(adjacency)
        for key, o in offsets.items():
            i = elf[0] + o[0]
            j = elf[1] + o[1]
            if bigger[i][j] == '#':
                flag = True
                a[key] = True
        if flag:
            found = False
            for rule in rules:
                if not a[rule[0]] and not a[rule[1]] and not a[rule[2]]:
                    o = offsets[rule[3]]
                    n = (elf[0] + o[0], elf[1] + o[1])
                    proposals.append(n)
                    found = True
                    break
            if not found:
                proposals.append((elf[0], elf[1]))
        else:
            proposals.append((elf[0], elf[1]))


    for e in range(len(proposals)):
        p1 = proposals[e]
        
        flag = True
        for o in range(len(proposals)):
            p2 = proposals[o]
            if e != o and p1 == p2:
                flag = False
                break

        if flag:
            bigger[elves[e][0]][elves[e][1]] = '.'
            bigger[p1[0]][p1[1]] = '#'
                
    r = rules.pop(0)
    rules.append(r)

    if backup == bigger: #part 2
        print(roundnum+1)
        break

#for row in bigger:
#    for col in row:
#        print(col, end='')
#    print()


def part1():
    min_i, min_j, max_i, max_j = float('inf'), float('inf'), -float('inf'), -float('inf')

    for i in range(len(bigger)):
        for j in range(len(bigger[i])):
            if bigger[i][j] == '#':
                min_i = min(i, min_i)
                min_j = min(j, min_j)
                max_i = max(i, max_i)
                max_j = max(j, max_j)

    count = 0
    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            if bigger[i][j] == '.':
                count += 1

    print(count)

#part1()
#part2 986 after some time :)
        
            
                
    

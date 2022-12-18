import copy

cave = [list("+-------+")]
empty = list("|.......|")
rocks = []
rocks.append([list("|..@@@@.|")])
rocks.append([list("|...@...|"), list("|..@@@..|"), list("|...@...|")])
rocks.append([list("|....@..|"), list("|....@..|"), list("|..@@@..|")])
rocks.append([list("|..@....|"), list("|..@....|"), list("|..@....|"), list("|..@....|")])
rocks.append([list("|..@@...|"), list("|..@@...|")])


moves = ""
with open("day17.txt") as day_file:
    moves = day_file.readline().strip()

def find_top():
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            if cave[i][j] == '#' or cave[i][j] == '-':
                return i

def find_indices():
    indices = []
    right_most = (0, 0)
    left_most = (0, 10)
    bottom_most = (0, 0)
    for i in range(len(cave)):
        found_some = False
        for j in range(len(cave[i])):
            if cave[i][j] == '@':
                found_some = True
                indices.append((i, j))

                if j > right_most[1]:
                    right_most = (i, j)

                if j < left_most[1]:
                    left_most = (i, j)

                if i > bottom_most[0]:
                    bottom_most = (i, j)
        if not found_some:
            break
    return indices, right_most, left_most, bottom_most

def print_cave():
    for row in cave:
        for col in row:
            print(col, end="")
        print()
    print()


#PART-2
memory = []
heights

count = 0
move = 0
rock_type = 0
while count < 1000000000000:
    #print_cave()
    top_index = find_top()
    if top_index > 3:
        cave = cave[top_index-3:]
    else:
        cave = [copy.deepcopy(empty) for _ in range (3-top_index)] + cave
    count += 1

    if count > 20:
        if (cave[:20], rock_type) in cave_memory:
            print("REPEATS")
            break
        cave_memory.append((cave[:20], rock_type))
    
    cave = copy.deepcopy(rocks[rock_type]) + cave
    rock_type = (rock_type + 1) % len(rocks)
    
    current_indices, right, left, bottom = find_indices()
    while True:
        #print_cave()
        #print(current_indices)

        new_indices = []
        if moves[move] == '>':
            blocked = False 
            for idx in current_indices:
                if cave[idx[0]][idx[1] + 1] == '#' or cave[idx[0]][idx[1] + 1] == '|':
                    blocked = True
                    break
            if not blocked:
                for idx in current_indices:
                    cave[idx[0]][idx[1]] = "."
                for idx in current_indices:
                    cave[idx[0]][idx[1] + 1] = "@"
                    new_indices.append((idx[0], idx[1] + 1))

        if moves[move] == '<':
            blocked = False 
            for idx in current_indices:
                if cave[idx[0]][idx[1] - 1] == '#' or cave[idx[0]][idx[1] - 1] == '|':
                    blocked = True
                    break
            if not blocked:
                for idx in current_indices:
                    cave[idx[0]][idx[1]] = "."
                for idx in current_indices:
                    cave[idx[0]][idx[1] - 1] = "@"
                    new_indices.append((idx[0], idx[1] - 1))

        if new_indices:
            current_indices = copy.deepcopy(new_indices)
            new_indices = []

        move = (move + 1) % len(moves)
        blocked = False
        for idx in current_indices:
            if cave[idx[0] + 1][idx[1]] == '#' or cave[idx[0] + 1][idx[1]] == '-':
                blocked = True
                break

        if not blocked:
            for idx in current_indices:
                cave[idx[0]][idx[1]] = "."
            for idx in current_indices:
                cave[idx[0] + 1][idx[1]] = "@"
                new_indices.append((idx[0] + 1, idx[1]))
            current_indices = copy.deepcopy(new_indices)
        else:
            for idx in current_indices:
                cave[idx[0]][idx[1]] = "#"
            break


#print_cave()
#part1
top_index = find_top()
print(len(cave) - top_index - 1)
        
        
#1571264367816 too low
#1571264368000 too low
#1571280000000 too low

    
    

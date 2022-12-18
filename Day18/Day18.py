max_x, max_y, max_z = 0, 0, 0

cubes = []
with open("day18.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        coords = line.split(',')
        max_x = max(int(coords[0]), max_x)
        max_y = max(int(coords[1]), max_y)
        max_z = max(int(coords[2]), max_z)
        cubes.append((int(coords[0]), int(coords[1]), int(coords[2])))
        line = day_file.readline().strip() 

def find_top():
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            if cave[i][j] == '#' or cave[i][j] == '-':
                return i


grid = [[[False for k in range(max_z + 2)] for j in range(max_y + 2)] for i in range(max_x + 2)]

print(max_x, max_y, max_y)

print(len(grid))
print(len(grid[0]))
print(len(grid[0][0]))
print(grid[0][0][0])

for c in cubes:
    grid[c[0]][c[1]][c[2]] = True


def water():
    stack = [(0, 0, 0), (max_x+1, 0, 0), (0, max_y+1, 0), (0, 0, max_z+1)]
    while stack:
        c = stack.pop()

        for x in range(c[0]-1, c[0]+2):
            for y in range(c[1]-1, c[1]+2):
                for z in range(c[2]-1, c[2]+2):
                    delta = (abs(c[0] - x), abs(c[1] - y), abs(c[2] - z))
                    if sum(delta) != 1:
                        continue
                    if x >= 0 and y >= 0 and z >= 0 and x < len(grid) and y < len(grid[x]) and z < len(grid[x][y]):
                        if not grid[x][y][z]:
                            grid[x][y][z] = 9999
                            stack.append((x, y, z))

water() #part2            
area = 0
for c in cubes:
    for x in range(c[0]-1, c[0]+2):
        for y in range(c[1]-1, c[1]+2):
            for z in range(c[2]-1, c[2]+2):
                delta = (abs(c[0] - x), abs(c[1] - y), abs(c[2] - z))
                if sum(delta) != 1:
                    continue
                if x >= 0 and y >= 0 and z >= 0 and x < len(grid) and y < len(grid[x]) and z < len(grid[x][y]):
                    if grid[x][y][z] == 9999:
                        area += 1
                else:
                    area += 1

print(area)

#4608 part1
    
#4500 too high
#4338 too high?!
#2628 too low 
#2652 part2

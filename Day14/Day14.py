class Path:
    def __init__(self):
        xs = []
        ys = []

    def draw(self):
        global G, min_x, min_y
        for i in range(len(self.xs) - 1):
            x1 = self.xs[i] - min_x
            x2 = self.xs[i+1] - min_x
            y1 = self.ys[i] - min_y
            y2 = self.ys[i+1] - min_y

            if x1 == x2:
                if y2 > y1:
                    for y in range(y1, y2+1):
                        G[y][x1] = '#'
                else:
                    for y in range(y2, y1+1):
                        G[y][x1] = '#'

            elif y1 == y2:
                if x2 > x1:
                    for x in range(x1, x2+1):
                        G[y1][x] = '#'
                else:
                    for x in range(x2, x1+1):
                        G[y1][x] = '#'

            else:
                print('DIAG?!')

paths = []

with open("day14.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        splitted = line.split('->')
        xs, ys = [],[]
        for corners in splitted:
            coords = corners.split(',')
            xs.append(int(coords[0]))
            ys.append(int(coords[1]))

        p = Path()
        p.xs = xs
        p.ys = ys
        paths.append(p)
            
        line = day_file.readline().strip()


print(len(paths))

min_x = min([min(p.xs) for p in paths]) - 300
max_x = max([max(p.xs) for p in paths]) + 300
min_y = 0
max_y = max([max(p.ys) for p in paths]) + 2

print(min_x, max_x, min_y, max_y)

SIZEX = max_x - min_x + 1
SIZEY = max_y - min_y + 1

G = []

for i in range(SIZEY):
    G.append(['.'] * SIZEX)

sand_x = 500 - min_x
G[0][sand_x] = '+'

for p in paths:
    p.draw()

#part 2
xs = [min_x, max_x]
ys = [max_y, max_y]
floor = Path()
floor.xs = xs
floor.ys = ys
floor.draw()

#for row in G:
#    print(row)

#######################################################

s = 0
abyss = False

while not abyss:
    #for row in G:
    #    print(row)
    #print()
    sand_x = 500 - min_x
    sand_y = 0
    while True:
        last_x = sand_x
        last_y = sand_y

        try:
            if G[sand_y + 1][sand_x] == '.':
                sand_y += 1
            elif G[sand_y + 1][sand_x - 1] == '.':
                sand_y += 1
                sand_x -= 1
            elif G[sand_y + 1][sand_x + 1] == '.':
                sand_y += 1
                sand_x += 1

            if last_x == sand_x and last_y == sand_y:
                break
        except:
            abyss = True
            break
    
    s += 1
    if G[sand_y][sand_x] == '+':
        print('part 2')
        s += 1
        break
    G[sand_y][sand_x] = 'o'

print(s-1)













    
    

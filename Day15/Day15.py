def manhattan(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

sensors = []
beacons = []

max_x = 0
max_y = 0
min_x = float('inf')
min_y = float('inf')
max_distance = 0

with open("day15.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        splitted = line.split(':')
        splitted[0] = splitted[0][9:]
        splitted[1] = splitted[1][21:]

        sensor_coords = splitted[0].split(',')
        sensor_x = int(sensor_coords[0].split('=')[1])
        sensor_y = int(sensor_coords[1].split('=')[1])
        
        line = day_file.readline().strip()
        #if sensor_y < 2000000 - 100 or sensor_y > 2000000 + 100: continue

        max_x = max(max_x, sensor_x)
        max_y = max(max_y, sensor_y)
        min_x = min(min_x, sensor_x)
        min_y = min(min_y, sensor_y)

        beacon_coords = splitted[1].split(',')
        beacon_x = int(beacon_coords[0].split('=')[1])
        beacon_y = int(beacon_coords[1].split('=')[1])

        max_x = max(max_x, beacon_x)
        max_y = max(max_y, beacon_y)
        min_x = min(min_x, beacon_x)
        min_y = min(min_y, beacon_y)

        sensors.append((sensor_x, sensor_y))
        beacons.append((beacon_x, beacon_y))
        max_distance = max(max_distance, manhattan((sensor_x, sensor_y), (beacon_x, beacon_y)))



def prepare():
    mapa = []
    for y in range(min_y, max_y+1):
        row = []
        for x in range(min_x, max_x+1):
            flag = False
            for i in range(len(sensors)):
                if sensors[i][0] == x and sensors[i][1] == y:
                    row.append('S')
                    flag = True
                    break
                if beacons[i][0] == x and beacons[i][1] == y:
                    flag = True
                    row.append('B')
                    break
            if not flag:
                row.append('.')
        mapa.append(row)
    return mapa


def draw():
    for row in M:
        for c in row:
            print(c, end="")
        print()

def areas(M):
    for i in range(len(sensors)):
        s = sensors[i]
        b = beacons[i]
        distance = manhattan(s, b)

        shifted_x = s[0] - min_x
        shifted_y = s[1] - min_y

        for y in range(shifted_y - distance - 1, shifted_y + distance + 1):
            for x in range(shifted_x - distance - 1, shifted_x + distance + 1):
                if y < 0 or x < 0 or y >= len(M) or x >= len(M[0]):
                    continue
                if M[y][x] == '.' and manhattan((shifted_x, shifted_y), (x, y)) <= distance:
                    M[y][x] = '#'
    return M

print(len(sensors))
goal_y = 10
suma = 0

#print(beacons)
#min_x -= 5
#min_y -= 5
#max_x += 5
#max_y += 5
#M = prepare()
#M = areas(M)
#draw()
#for x in range(len(M[goal_y])):
    #print(M[goal_y][x], end="")
#    if M[goal_y][x] == '#':
#        suma += 1

def part1():
    global suma
    for x in range(min_x - max_distance, max_x + max_distance):
        if x % 100000 == 0:
            print(x / max_x)
        occupied = False
        for i in range(len(sensors)):
            s = sensors[i]
            b = beacons[i]
            if manhattan(s, (x, goal_y)) <= manhattan(s, b):
                occupied = True
                break
        if occupied:
            suma += 1
    print()  
    print(suma)    

#part1()
#5144287
#5144286

def check(x, y):
    if x >= low_bound and x <= up_bound and y >= low_bound and y <= up_bound:
        for k in range(len(sensors)):
            if manhattan(sensors[k], (x, y)) <= distances[k]:
                return False

        print(x ,y)
        print(4000000 * x + y)
        return True
    return False

def part2():    
    for i in range(len(sensors)):
        print("perimeter of sensor: ", i)
        d = distances[i]
        s = sensors[i]
        dx = d+1
        dy = 0

        for _ in range(d+2):
            if check(s[0] + dx, s[1] + dy) or check(s[0] + dx, s[1] - dy) or check(s[0] - dx, s[1] + dy) or check(s[0] - dx, s[1] - dy):
                return

            dx -= 1
            dy += 1


distances = []
for i in range(len(sensors)):
    s = sensors[i]
    b = beacons[i]
    d = manhattan(s, b)
    distances.append(d)
      
low_bound = 0
up_bound = 4000000
part2()
#10229191267339
 


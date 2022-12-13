
visited = set()
#head = (0, 0)
#tail = (0, 0)
knots = [(0, 0) for _ in range(10)]

def move(head, tail):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:

        if head[0] == tail[0] + 2 and head[1] == tail[1]: #right
            tail = (tail[0] + 1, tail[1])

        elif head[0] == tail[0] - 2 and head[1] == tail[1]: #left
            tail = (tail[0] - 1, tail[1])

        elif head[1] == tail[1] - 2 and head[0] == tail[0]: #up
            tail = (tail[0], tail[1] - 1)

        elif head[1] == tail[1] + 2 and head[0] == tail[0]: #down
            tail = (tail[0], tail[1] + 1)


        elif head[0] == tail[0] - 2 and head[1] == tail[1] - 1:
            tail = (tail[0] - 1, tail[1] - 1)

        elif head[0] == tail[0] - 1 and head[1] == tail[1] - 2:
            tail = (tail[0] - 1, tail[1] - 1)

        elif head[0] == tail[0] + 1 and head[1] == tail[1] + 2:
            tail = (tail[0] + 1, tail[1] + 1)

        elif head[0] == tail[0] + 2 and head[1] == tail[1] + 1:
            tail = (tail[0] + 1, tail[1] + 1)

        elif head[0] == tail[0] + 2 and head[1] == tail[1] - 1:
            tail = (tail[0] + 1, tail[1] - 1)

        elif head[0] == tail[0] + 1 and head[1] == tail[1] - 2:
            tail = (tail[0] + 1, tail[1] - 1)

        elif head[0] == tail[0] - 2 and head[1] == tail[1] + 1:
            tail = (tail[0] - 1, tail[1] + 1)

        elif head[0] == tail[0] - 1 and head[1] == tail[1] + 2:
            tail = (tail[0] - 1, tail[1] + 1)

        # PART-2 DIAGONALS
        elif head[0] == tail[0] - 2 and head[1] == tail[1] - 2:
            tail = (tail[0] - 1, tail[1] - 1)

        elif head[0] == tail[0] + 2 and head[1] == tail[1] - 2:
            tail = (tail[0] + 1, tail[1] - 1)

        elif head[0] == tail[0] + 2 and head[1] == tail[1] + 2:
            tail = (tail[0] + 1, tail[1] + 1)

        elif head[0] == tail[0] - 2 and head[1] == tail[1] + 2:
            tail = (tail[0] - 1, tail[1] + 1)

    return tail


with open("day9.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        direction, amount = line.split(' ')

        for i in range(int(amount)):
            if direction == 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direction == 'U':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            elif direction == 'D':
                knots[0] = (knots[0][0], knots[0][1] + 1)


            for i in range(1, 10):
                knots[i] = move(knots[i-1], knots[i])


            visited.add(knots[9])
                     
        line = day_file.readline().strip()

print(knots)
print(len(visited))





    



            
        

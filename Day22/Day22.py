import copy

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


max_length = 0
with open("day22.txt") as day_file:
    line = day_file.readline()
    while line:
        max_length = max(max_length, len(line))
        line = day_file.readline()

print(max_length)

board = []
directions = []
with open("day22.txt") as day_file:
    line = day_file.readline().replace(' ', 'o')
    line = line[:-1] + "o" * (max_length - len(line)) 
    while line:
        board.append(line)
        line = day_file.readline().replace(' ', 'o')
        if not line or len(line) < 2:
            break
        line =line[:-1] + "o" * (max_length - len(line))
    

    line = day_file.readline()
    number = ""
    for d in line:
        if d in "0123456789":
            number += d
        else:
            if number:
                directions.append(int(number))
                number = ""
            if d != '\n':
                directions.append(d)

#for line in board:
#    print(line)

#print(directions)

c = (0, None)
h = 0 
for col in range(len(board[0])):
    if board[0][col] == ".":
        c = (0, col)
        break

for d in directions:
    if type(d) == str:
        if d == "R":
            h += 1
            if h > 3:
                h = 0
        elif d == "L":
            h -= 1
            if h < 0:
                h = 3
    else:
        #print(c)
        #print(h)
        wall = False
        if h == 0: #right
            for i in range(d):
                if wall: break
                if c[1] + 1 >= len(board[c[0]]) or board[c[0]][c[1] + 1] == "o":
                    for col in range(len(board[c[0]])):
                        if board[c[0]][col] == '.':
                            c = (c[0], col)
                            break
                        elif board[c[0]][col] == '#':
                            wall = True
                            break
                elif board[c[0]][c[1] + 1] == ".":
                    c = (c[0], c[1] + 1)
                else:
                    wall = True
                    
        elif h == 1: #down
            for i in range(d):
                if wall: break
                if c[0] + 1 >= len(board) or board[c[0] + 1][c[1]] == "o":
                    for row in range(len(board)):
                        if board[row][c[1]] == '.':
                            c = (row, c[1])
                            break
                        elif board[row][c[1]] == '#':
                            wall = True
                            break
                elif board[c[0] + 1][c[1]] == ".":
                    c = (c[0] + 1, c[1])
                else:
                    wall = True
                    
        elif h == 2: #left
            for i in range(d):
                if wall: break
                if c[1] - 1 < 0 or board[c[0]][c[1] - 1] == "o":
                    for col in range(len(board[c[0]])-1, -1, -1):
                        if board[c[0]][col] == '.':
                            c = (c[0], col)
                            break
                        elif board[c[0]][col] == '#':
                            wall = True
                            break
                elif board[c[0]][c[1] - 1] == ".":
                    c = (c[0], c[1] - 1)
                else:
                    wall = True
                    
        elif h == 3: #up
            for i in range(d):
                if wall: break
                if c[0] - 1 < 0 or board[c[0] - 1][c[1]] == "o":
                    for row in range(len(board)-1, -1, -1):
                        if board[row][c[1]] == '.':
                            c = (row, c[1])
                            break
                        elif board[row][c[1]] == '#':
                            wall = True
                            break
                elif board[c[0] - 1][c[1]] == ".":
                    c = (c[0] - 1, c[1])
                else:
                    wall = True
    

print(1000 * (c[0] + 1) + 4 * (c[1] + 1) + h)

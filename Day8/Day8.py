

grid = []

with open("day8.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        grid.append([int(height) for height in line])
        line = day_file.readline().strip()



##inside = 0
##for row in range (1, len(grid)- 1):
##    for col in range(1, len(grid[0]) - 1):
##        up_visible, down_visible, left_visible, right_visible = True, True, True, True
##        current = grid[row][col]
##        
##        for up in range(0, row):
##            if grid[up][col] >= current:
##                up_visible = False
##                break
##
##        for down in range(row+1, len(grid)):
##            if grid[down][col] >= current:
##                down_visible = False
##                break
##
##        for left in range(0, col):
##            if grid[row][left] >= current:
##                left_visible = False
##                break
##
##        for right in range(col+1, len(grid[0])):
##            if grid[row][right] >= current:
##                right_visible = False
##                break
##                
##        if up_visible or down_visible or left_visible or right_visible:
##            inside += 1
##
##print(inside + len(grid) * 2 + len(grid[0]) * 2 - 4)
        

max_score = 0
for row in range (1, len(grid)- 1):
    for col in range(1, len(grid[0]) - 1):
        up_score, down_score, left_score, right_score = 0, 0, 0, 0
        current = grid[row][col]

        for up in range(1, row+1):
            up_score += 1
            if grid[row-up][col] >= current:
                break

        for down in range(row+1, len(grid)):
            down_score += 1
            if grid[down][col] >= current:
                break

        for left in range(1, col+1):
            left_score += 1
            if grid[row][col-left] >= current:
                break

        for right in range(col+1, len(grid[0])):
            right_score += 1
            if grid[row][right] >= current:
                break

        total = up_score * down_score * left_score * right_score
        if total > max_score:
            max_score = total
            #print(row)
            #print(col)
            #print(up_score)
            #print(down_score)
            #print(left_score)
            #print(right_score)
            #print()


print(max_score)
    



            
        

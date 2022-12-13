
##strength = 0
##cycle = 1
##val = 1
##
##with open("day10.txt") as day_file:
##    line = day_file.readline().strip()
##    while line:
##        add_amount = 0
##        
##        if line == 'noop':
##            cycle += 1
##            
##        else:
##            splitted = line.split(' ')
##            cycle += 1
##            if cycle in [20, 60, 100, 140, 180, 220]:
##                strength += cycle * val
##            cycle += 1
##            add_amount = int(splitted[1])
##
##        val += add_amount
##
##        if cycle in [20, 60, 100, 140, 180, 220]:
##            strength += cycle * val
##        
##        line = day_file.readline().strip()
##
##
##print(strength)


cycle = 1
val = 1
current_line = ''
current_pixel = 0

def CRT_DRAW():
    global val, current_line, current_pixel
    if current_pixel == val-1 or current_pixel == val or current_pixel == val+1:
        current_line += '#'
    else:
        current_line += '.'
    current_pixel += 1
    if current_pixel > 39:
        print(current_line)
        current_line = ''
        current_pixel = 0

with open("day10.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        add_amount = 0
        
        if line == 'noop':
            CRT_DRAW()
            cycle += 1
            
        else:
            splitted = line.split(' ')
            CRT_DRAW()
            cycle += 1
            CRT_DRAW()
            cycle += 1
            add_amount = int(splitted[1])

        val += add_amount

        line = day_file.readline().strip()


#RUAKHBEK


            
        

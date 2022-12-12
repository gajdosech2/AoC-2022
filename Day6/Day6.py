with open("day6.txt") as day_file:
    line = day_file.readline().strip()
    character = 0
    last = []
    for c in line:
        last.append(c)
        character += 1
        if len(last) > 14:
            last = last[1:]
            
        if len(last) == 14 and len(set(last)) == len(last): #part 1 -> len(last) == 4
            break

print(character)


        

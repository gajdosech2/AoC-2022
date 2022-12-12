##
##suma = 0
##with open("day3.txt") as day_file:
##    line = day_file.readline().strip()
##    while line:
##        comp1 = line[:int(len(line)/2)]
##        comp2 = line[int(len(line)/2):]
##        for item in comp1:
##            if item in comp2:
##                #print(item)
##                if item.isupper():
##                    suma += ord(item) - ord('A') + 27
##                else:
##                    suma += ord(item) - ord('a') + 1
##                break
##        line = day_file.readline().strip()
##
##print(suma)

lines = []
line_num = 1
suma = 0
with open("day3.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        lines.append(line)
        if line_num % 3 == 0:
            for item in lines[0]:
                if item in lines[1] and item in lines[2]:
                    #print(item)
                    if item.isupper():
                        suma += ord(item) - ord('A') + 27
                    else:
                        suma += ord(item) - ord('a') + 1
                    break
            lines = []
        line = day_file.readline().strip()
        line_num += 1

print(suma)

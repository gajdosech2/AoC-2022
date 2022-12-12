##
##count = 0
##with open("day4.txt") as day_file:
##    line = day_file.readline().strip()
##    while line:
##        pair_split = line.split(',')
##        elf1_range = pair_split[0].split('-')
##        elf2_range = pair_split[1].split('-')
##        if int(elf1_range[0]) <= int(elf2_range[0]) and int(elf2_range[1]) <= int(elf1_range[1]):
##            count += 1
##        elif int(elf2_range[0]) <= int(elf1_range[0]) and int(elf1_range[1]) <= int(elf2_range[1]):
##            count += 1
##        line = day_file.readline().strip()
##
##
##print(count)


count = 0
with open("day4.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        pair_split = line.split(',')
        elf1_range = pair_split[0].split('-')
        elf2_range = pair_split[1].split('-')
        if set(range(int(elf1_range[0]), int(elf1_range[1]) + 1)).intersection(set(range(int(elf2_range[0]), int(elf2_range[1]) + 1))):
            count += 1
        line = day_file.readline().strip()
        

print(count)

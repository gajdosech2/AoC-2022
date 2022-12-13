import ast

CORRECT = 1
WRONG = 2
SAME = 3

def compare(p1, p2):
    if type(p1) == type(1) and type(p2) == type(1):
        if p1 == p2:
            return SAME
        if p1 < p2:
            return CORRECT
        if p1 > p2:
            return WRONG
        
    if type(p1) == type([1,2]) and type(p2) == type(1):
        p2 = [p2]
    if type(p2) == type([1,2]) and type(p1) == type(1):
        p1 = [p1]

    lp1 = len(p1)
    lp2 = len(p2)

    length = min(lp1, lp2)

    for i in range(length):
        res = compare(p1[i], p2[i])
        if res == CORRECT:
            return CORRECT
        if res == WRONG:
            return WRONG

    if lp1 == lp2:
        return SAME
    if lp1 < lp2:
        return CORRECT
    if lp1 > lp2:
        return WRONG

##
##total = 0
##with open("day13.txt") as day_file:
##    line = day_file.readline().strip()
##    last_line = ""
##    pair_idx = 1
##    while line or last_line:
##        if line and last_line:
##            p1 = ast.literal_eval(last_line)
##            p2 = ast.literal_eval(line)
##            res = compare(p1, p2)
##            #print(res)
##            if res == CORRECT:
##                total += pair_idx
##            pair_idx += 1
##        last_line = line
##        line = day_file.readline().strip()
##
##print(total)


packets = [ [[2]] , [[6]] ]
with open("day13.txt") as day_file:
    line = day_file.readline().strip()
    last_line = ""
    while line or last_line:
        if line:
            packet = ast.literal_eval(line)
            packets.append(packet)
        last_line = line
        line = day_file.readline().strip()


def switch(packetz, i, j):
    packetz[i], packetz[j] = packetz[j], packetz[i]

def bubble_sort(packetz):
    for i in range(len(packetz)):
        for j in range(len(packetz)-1):
            if compare(packetz[j], packetz[j+1]) == WRONG:
                switch(packetz, j, j+1)

bubble_sort(packets)

idx1, idx2 = -1, -1
for i in range(len(packets)):
    packet = packets[i]
    if packet == [[2]] and idx1 == -1:
        idx1 = i + 1

    if packet == [[6]] and idx2 == -1:
        idx2 = i + 1
        break

print(idx1)
print(idx2)
print(idx1 * idx2)

















    
    

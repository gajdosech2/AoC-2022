class Valve:
    def __init__(self):
        self.name = ""
        self.other = list()
        self.neigh = list()
        self.rate = 0

    def __repr__(self):
        return f'<{self.name}, {self.other}, {self.neigh}, {self.rate}>'

    def __str__(self):
        return f'<{self.name}, {self.other}, {self.neigh}, {self.rate}>'
    

valves = []
with open("day16.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        splitted = line.split(';')
        name = splitted[0][6:8]
        rate = int(splitted[0].split('=')[1])

        if 'valves' in splitted[1]:
            other = splitted[1].split('valves')[1].strip().split(',')
        else:
            other = splitted[1].split('valve')[1].strip().split(',')        
        other = [o.strip() for o in other]
        
        v = Valve()
        v.name = name 
        v.other = other
        v.rate = rate
        valves.append(v)
        line = day_file.readline().strip()
    

starting_valve = None
for v in valves:
    if v.name == 'AA':
        starting_valve = v
    for n in v.other:
        for o in valves:
            if n == o.name:
                v.neigh.append(o)
    #print(v)

def part1():
    memory = dict()
    best = 0
    stack = [(starting_valve, 1, 0, set())]

    while stack:
        v, time, score, opened = stack.pop()
        if (v, time) not in memory or memory[(v, time)] < score:
            memory[(v, time)] = score
            if time == 30:
                best = max(best, score)
                continue

            if v.rate > 0 and v not in opened:
                new_opened = opened.copy()
                new_opened.add(v)
                new_score = score + sum(o.rate for o in new_opened)
                new_state = (v, time+1, new_score, new_opened)
                stack.append(new_state)

            new_score = score + sum(o.rate for o in opened)
            for n in v.neigh:
                new_state = (n, time+1, new_score, opened)
                stack.append(new_state)
                
               
    return best


res = part1()
print(res)

# 1797 too low - wrong start, AA is not first in the list
# 1906

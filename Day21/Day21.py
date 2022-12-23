import copy

class Monkey:
    def __init__(self):
        self.name = None
        self.m1name = None
        self.m1 = None
        self.m2name = None
        self.m2 = None
        self.op = None
        self.res = None

    def eval(self, depth=0):
        if self.res:
            return self.res

        if depth > 0:
            return None
  
        if self.m1 and not self.m1.res:
            self.m1.eval(1)

        if self.m2 and not self.m2.res:
            self.m2.eval(1)
        
        if self.m1.res and self.m2.res:
            if self.name == "root":
                self.res = self.m1.res == self.m2.res
            elif self.op == "+":
                self.res = self.m1.res + self.m2.res
            elif self.op == "-":
                self.res = self.m1.res - self.m2.res
            elif self.op == "*":
                self.res = self.m1.res * self.m2.res
            elif self.op == "/":
                self.res = int(self.m1.res / self.m2.res)

            return self.res
        
        return None

    def __str__(self):
        return self.name + ";" + str(self.res) + ";" + str(self.m1name) + ';' + str(self.op) + ";" + str(self.m2name)

    def __repr__(self):
        return self.name + ";" + str(self.res) + ";" + str(self.m1name) + ';' + str(self.op) + ";" + str(self.m2name)
                  

monkeys = []
with open("day21.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        name, op = line.split(":")
        res, o, m1name, m2name = None, None, None, None
        
        if "+" in op:
            o = "+"
            m1name, m2name = op.strip().split(" + ")
        elif "-" in op:
            o = "-"
            m1name, m2name = op.strip().split(" - ")
        elif "*" in op:
            o = "*"
            m1name, m2name = op.strip().split(" * ")
        elif "/" in op:
            o = "/"
            m1name, m2name = op.strip().split(" / ")
        else:
            res = int(op)

        m = Monkey()
        m.name = name
        m.m1name = m1name
        m.m2name = m2name
        m.op = o
        m.res = res
        monkeys.append(m)
        line = day_file.readline().strip()


#for m in monkeys:
#    print(m)


def initialize(monkeys_copy):
    you = None
    root = None
    for m in monkeys_copy:
        if m.name == "root":
            root = m
        if m.name == "humn":
            you = m
        if m.m1name and m.m2name:
            m1, m2 = None, None
            for o in monkeys_copy:
                if o.name == m.m1name:
                    m1 = o
                if o.name == m.m2name:
                    m2 = o
            m.m1 = m1
            m.m2 = m2
    return you, root


def evaluate(root, monkeys):
     while root.res == None:
        for m in monkeys:
            #print(m.name, end=":::")
            res = m.eval()
            #print(res)

lower = 0
upper = 1000000000000000
while True:
    yelling = (upper + lower) // 2
    print(yelling)
    
    m_copy = copy.deepcopy(monkeys)
    you, root = initialize(m_copy)
    you.res = yelling
    evaluate(root, m_copy)

    left = root.m1.res
    right = root.m2.res

    if root.res:
        print("SUCCESS")
        print(left)
        print(right)
        print(yelling)
        break

    if left > right:
        lower = yelling

    if right > left:
        upper = yelling
    

#38914458159166
#3665520865940

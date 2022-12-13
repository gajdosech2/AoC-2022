class Monkey:
    def __init__(self):
        self.items = []
        self.operator = ''
        self.operant = -1
        self.divider = -1
        self.monkey_true = -1
        self.monkey_false = -1
        self.activity = 0

    def turn(self):
        global monkeys
        for item in self.items:
            worry = self.inspect(item)
            test = worry % self.divider == 0
            if test:
                monkeys[self.monkey_true].items.append(worry)
            else:
                monkeys[self.monkey_false].items.append(worry)

        self.items = []

    def __repr__(self):
        return f'{self.items}, {self.operator}, {self.operant}, {self.divider}, {self.monkey_true}, {self.monkey_false}'

    def __str__(self):
        return f'{self.items}, {self.operator}, {self.operant}, {self.divider}, {self.monkey_true}, {self.monkey_false}'

    def inspect(self, item):
        self.activity += 1
        worry = 0
        if self.operator == '*':
            if self.operant == "old":
                worry = item * item
            else:
                worry = item * self.operant
            
        if self.operator == '+':
            if self.operant == "old":
                worry = item + item
            else:
                worry = item + self.operant

        #worry = int(worry / 3) #part1
        worry = int(worry % worry_dividor)
        return worry


monkeys = []

with open("day11.txt") as day_file:
    while True:
        line1 = day_file.readline().strip()
        if not line1:
            break
        line2 = day_file.readline().strip()
        line3 = day_file.readline().strip()
        line4 = day_file.readline().strip()
        line5 = day_file.readline().strip()
        line6 = day_file.readline().strip()
        line7 = day_file.readline().strip()

        items = eval('[' + line2.split(':')[1].strip() + ']')
        line3 = line3.split('=')[1].strip()
        if '*' in line3:
            line3 = line3.split('*')[1].strip()
            operator = '*'
        if '+' in line3:
            line3 = line3.split('+')[1].strip()
            operator = '+'

        if line3 == "old":
            operant = "old"
        else:
            operant = int(line3)


        divider = int(line4.split("by")[1].strip())
        
        monkey_true = int(line5[-1])
        monkey_false = int(line6[-1])

        monkey = Monkey()
        monkey.items = items
        monkey.operator = operator
        monkey.operant = operant
        monkey.divider = divider
        monkey.monkey_true = monkey_true
        monkey.monkey_false = monkey_false
        monkeys.append(monkey)


for m in monkeys:
#    print(m)
    print(m.divider)

#worry_dividor = 96577
worry_dividor = 9699690

for r in range(10000):
    for m in range(len(monkeys)):
        monkeys[m].turn()

    #print("round:", r)
    #for m in monkeys:
    #    print(m.items)

for m in monkeys:
    print(m.activity)



            
        

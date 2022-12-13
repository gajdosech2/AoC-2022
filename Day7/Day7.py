
class Node:
    def __init__(self):
        self.children = []
        self.parent = None
        self.name = ""
        self.content = ""

    def size(self):
        if self.content == "dir":
            total = 0
            for child in self.children:
                total += child.size()
            return total
        else:
            return int(self.content)


root = Node()
root.name = "/"
root.content = "dir"

current = None
ls = []
with open("day7.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        if line[0] == '$':
            if ls:
                current.children += ls
                ls = []

            command = line[2:]
            if command != "ls":
                splitted = command.split(' ')
                if splitted[1] == '/':
                    current = root
                elif splitted[1] == '..':
                    current = current.parent
                else:
                    for child in current.children:
                        if child.name == splitted[1]:
                            current = child
                            break
        else:
            splitted = line.split(' ')
            if line[0] == 'd':
                new_dir = Node()
                new_dir.name = splitted[1]
                new_dir.content = "dir"
                new_dir.parent = current
                ls.append(new_dir)
            else:
                new_file = Node()
                new_file.name = splitted[1]
                new_file.content = splitted[0]
                new_file.parent = current
                ls.append(new_file)

        line = day_file.readline().strip()

    if ls:
        current.children += ls

#print(root.size())

suma = 0
to_process = [root]

##while to_process:   
##    node = to_process.pop()
##    for child in node.children:
##        to_process.append(child)
##
##    if node.content == "dir":
##        size = node.size()
##        if size <= 100000:
##            suma += size


#print(suma)


total_space = 70000000
required = 30000000
free = total_space - root.size()
diff = required - free

current_best = root.size()
while to_process:   
    node = to_process.pop()
    for child in node.children:
        to_process.append(child)

    if node.content == "dir":
        size = node.size()
        if size >= diff and size <= current_best:
            current_best = size

print(current_best)





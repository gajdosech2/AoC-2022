import copy

class Vertex:
    ID = 0
    def __init__(self):
        self.elevation = 'a'
        self.neighbors = []
        self.ID = self.ID + 1
        self.num = self.ID

    def __str__(self):
        return self.elevation

    def __repr__(self):
        return self.elevation

visited = []
dist = []
G = []
start_coord = (0, 0)
end_coord = (0, 0)

with open("day12.txt") as day_file:
    line = day_file.readline().strip()
    y = 0
    while line:
        row = []
        x = 0
        for c in list(line):
            if c == 'S':
                start_coord = (y, x)
                c = 'a'
            elif c == 'E':
                end_coord = (y, x)
                c = 'z'

            new_vertex = Vertex()
            new_vertex.elevation = c
            row.append(new_vertex)
            x += 1

        dist.append([float('inf')] * len(row))
        visited.append([False] * len(row)) 
        G.append(row)
        y += 1
        line = day_file.readline().strip()

#print(start_coord)
#print(end_coord)

for i in range(len(G)):
    row = G[i]
    #print(row)
    #print(dist[i])
    #print()
    for j in range(len(row)):
        v = row[j]
        if i - 1 >= 0 and ord(G[i - 1][j].elevation) <= ord(v.elevation) + 1:
            v.neighbors.append(G[i - 1][j])
        if j - 1 >= 0 and ord(G[i][j - 1].elevation) <= ord(v.elevation) + 1:
            v.neighbors.append(G[i][j - 1])
        if i + 1 < len(G) and ord(G[i + 1][j].elevation) <= ord(v.elevation) + 1:
            v.neighbors.append(G[i + 1][j])
        if j + 1 < len(row)and ord(G[i][j + 1].elevation) <= ord(v.elevation) + 1:
            v.neighbors.append(G[i][j + 1])
        

#print(G[0][0].neighbors)

def djikstra(start_coord, dist, visited):
    global G, end_coord
    dist[start_coord[0]][start_coord[1]] = 0

    for _ in range(len(G)):
        for _ in range(len(G[0])):
    
            minimal = float('inf')
            k, l = 9999, 9999
            for i in range(len(G)):
                for j in range(len(G[i])):
                    if dist[i][j] < minimal and visited[i][j] == False:
                        minimal = dist[i][j]
                        k, l = i, j

            if k == 9999: #Not all vertex are accesible?!
                return dist
            visited[k][l] = True
            u = G[k][l]

            for i in range(max(0, k-1), min(k+2, len(G))):
                for j in range(max(0, l-1), min(l+2, len(G[k]))):
                    v = G[i][j]
                    if visited[i][j] == False and v in u.neighbors and dist[i][j] > dist[k][l] + 1:
                        dist[i][j] = dist[k][l] + 1

            if k == end_coord[0] and l == end_coord[1]:
                return dist

    return dist

best_route = 534
possible_starts = []
for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j].elevation == 'a':
            possible_starts.append((i, j))

print(len(possible_starts))
#res = djikstra(start_coord, copy.deepcopy(dist), copy.deepcopy(visited))
#print(res[end_coord[0]][end_coord[1]])

for i in range(len(possible_starts)):
    start = possible_starts[i]
    if i % 10 == 0:
        print("current", i)
    res = djikstra(start, copy.deepcopy(dist), copy.deepcopy(visited))
    value = res[end_coord[0]][end_coord[1]]
    if value < best_route:
        print("new best", value)
        best_route = value 

print(best_route)





            

            
        

import copy

blueprints = []

default_cost = {"ore": 0, "clay": 0, "obsidian": 0}
with open("day19.txt") as day_file:
    line = day_file.readline().strip()
    while line:
        blueprint = dict()

        ore_robot_cost = int(line.split("ore robot costs")[1].split("ore")[0].strip())
        blueprint["ore robot"] = default_cost.copy()
        blueprint["ore robot"]["ore"] = ore_robot_cost

        clay_robot_cost = int(line.split("clay robot costs")[1].split("ore")[0].strip())
        blueprint["clay robot"] = default_cost.copy()
        blueprint["clay robot"]["ore"] = clay_robot_cost

        obsidian_robot_cost_ore = int(line.split("obsidian robot costs")[1].split("ore")[0].strip())
        obsidian_robot_cost_clay = int(line.split("obsidian robot costs")[1].split("ore and")[1].split("clay")[0].strip())
        blueprint["obsidian robot"] = default_cost.copy()
        blueprint["obsidian robot"]["ore"] = obsidian_robot_cost_ore
        blueprint["obsidian robot"]["clay"] = obsidian_robot_cost_clay

        geode_robot_cost_ore = int(line.split("geode robot costs")[1].split("ore")[0].strip())
        geode_robot_cost_obsidian = int(line.split("geode robot costs")[1].split("ore and")[1].split("obsidian")[0].strip())
        blueprint["geode robot"] = default_cost.copy()
        blueprint["geode robot"]["ore"] = geode_robot_cost_ore
        blueprint["geode robot"]["obsidian"] = geode_robot_cost_obsidian
        blueprints.append(blueprint)
        line = day_file.readline().strip()

print(blueprints[0])
        

def evaluate_blueprint(b):
    best_geodes = 0
    earliest_time_1 = 34
    earliest_time_2 = 34
    earliest_time_3 = 34

    start_state = {"ore robot": 1, "clay robot": 0, "obsidian robot": 0, "geode robot": 0, "ore": 0, "clay": 0, "obsidian": 0, "geode": 0, "time": 1}
    queue = [start_state]
    while queue:
        s = queue.pop()

        #print(s["time"])
        if s["time"] >= 33:
            continue

        n = s.copy()
        n["time"] += 1
        #production
        
        if n["ore robot"]:
            n["ore"] += n["ore robot"]

        if n["clay robot"]:
            n["clay"] += n["clay robot"]

        if n["obsidian robot"]:
            n["obsidian"] += n["obsidian robot"]

        if n["geode robot"]:
            n["geode"] += n["geode robot"]

        if n["geode"] == 0 and n["time"] >= earliest_time_1:
            continue

        if n["geode"] == 1 and n["time"] >= earliest_time_2:
            continue

        if n["geode"] == 2 and n["time"] >= earliest_time_3:
            continue

        if n["geode"] == 1 and n["time"] < earliest_time_1:
            earliest_time_1 = n["time"]

        if n["geode"] == 2 and n["time"] < earliest_time_2:
            earliest_time_2 = n["time"]

        if n["geode"] == 3 and n["time"] < earliest_time_3:
            earliest_time_3 = n["time"]

        if n["geode"] > best_geodes:
            best_geodes = n["geode"]
            #print("new best", best_geodes)
        

        #branching

        if s["ore"] >= b["geode robot"]["ore"] and s["obsidian"] >= b["geode robot"]["obsidian"]:
            m = n.copy()
            m["ore"] -= b["geode robot"]["ore"]
            m["obsidian"] -= b["geode robot"]["obsidian"]
            m["geode robot"] += 1
            queue.append(m)

        if s["ore"] >= b["obsidian robot"]["ore"] and s["clay"] >= b["obsidian robot"]["clay"] and n["time"] < 29 and n["obsidian"] < 30:
            m = n.copy()
            m["ore"] -= b["obsidian robot"]["ore"]
            m["clay"] -= b["obsidian robot"]["clay"]
            m["obsidian robot"] += 1
            queue.append(m)

        if s["ore"] >= b["clay robot"]["ore"] and n["time"] < 26 and n["clay"] < 30:
            m = n.copy()
            m["ore"] -= b["clay robot"]["ore"]
            m["clay robot"] += 1
            queue.append(m)

        if s["ore"] >= b["ore robot"]["ore"] and n["time"] < 19 and n["ore"] < 30:
            m = n.copy()
            m["ore"] -= b["ore robot"]["ore"]
            m["ore robot"] += 1
            queue.append(m)

        queue.append(n)
    return best_geodes


#quality = 0
#for i in range(len(blueprints)):
#    print(i)
#    quality += evaluate_blueprint(blueprints[i]) * (i+1)
    
#evaluate_blueprint(blueprints[0])
#print(quality)

res = 1
for i in range(3):
    print("Blueprint: ", i)
    q = evaluate_blueprint(blueprints[i])
    res *= q
    print(q)

print(res)


#1406 too low
#1461 too low
#1528, finally good constants


#10*24*36=8640 too low part 2
#11*26*39=11154 too low part 2
#12*27*40=12960 too low part 2
#13*31*42=16926 after few hours :)


        

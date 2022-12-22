from time import perf_counter
from utils import *
from collections import deque

def solve(BP, T):
    ooc, coc, oboc, obcc, gcc, goc = BP.costs["ore"], BP.costs["clay"], BP.costs["obsidian"][0], BP.costs["obsidian"][1], BP.costs["geode"][0], BP.costs["geode"][1]
    best = 0
    # ore_ore_cost = ooc
    # clay_ore_cost = coc
    # obsidian_ore_cost = oboc
    # obsidian_clay_cost = obcc
    # geode_clay_cost = gcc
    # geode_obsidian_cost = goc

    # no need to buy more ore robots than the greatest cost
    max_ore = max([ooc, coc, oboc, gcc])
    # initial state and queue
    S = (0, 0, 0, 0, 1, 0, 0, 0, T)
    Q = deque([S])
    SEEN = set()
    while Q:
        state = Q.popleft()
        ore,clay,obi,geo,ore_robo,clay_robo,obi_robo,geo_robo,t = state
        # cant make more geodes than the current best if we build geo everyday
        if best + best > 2*(geo + geo_robo * t) + t * t - t:
            continue
        best = max(best, geo)
        # the last day doesnt allow for more robots as they wont work yet
        if t==1:
            best = max(best, geo + geo_robo)
            continue

        # reduce resources and robots to minimum required allow for more DP
        if ore_robo >= max_ore:
            ore_robo = max_ore
        if clay_robo >= obcc:
            clay_robo = obcc
        if obi_robo >= goc:
            obi_robo = goc
        # resources only need to be most expensive cost * time left - robot production
        if ore >= t * (max_ore - ore_robo) + ore_robo:
            ore = t * (max_ore - ore_robo) + ore_robo
        if clay >= t * (obcc - clay_robo) + clay_robo:
            clay = t * (obcc - clay_robo) + clay_robo
        if obi >= t * (goc - obi_robo) + obi_robo:
            obi = t * (goc - obi_robo) + obi_robo

        # check if we have seen this state before
        # time isnt needed as nothing requires geodes to build
        cc = (ore,clay,obi,geo,ore_robo,clay_robo,obi_robo,geo_robo)
        if cc in SEEN:
            continue
        SEEN.add(cc)

        # boolean check if we can build all robots
        check = 0
        # enough resources to build a geode robot
        if ore>=gcc and obi>=goc:
            # often best to build a geode robot so we append left
            check += 1
            Q.appendleft((ore - gcc + ore_robo, clay + clay_robo, obi - goc + obi_robo, geo + geo_robo, ore_robo, clay_robo, obi_robo, geo_robo + 1, t-1))
        # enough resources to build an obsidian robot
        if ore>=oboc and clay>=obcc:
            check += 2
            Q.append((ore - oboc + ore_robo, clay - obcc + clay_robo, obi + obi_robo, geo + geo_robo, ore_robo, clay_robo, obi_robo + 1, geo_robo, t-1))
        # enough resources to build a clay robot
        if ore>=coc:
            check += 4
            Q.append((ore - coc + ore_robo, clay + clay_robo, obi + obi_robo, geo + geo_robo, ore_robo, clay_robo + 1, obi_robo, geo_robo, t-1))
        # enough resources to build an ore robot
        if ore>=ooc:
            check += 8
            Q.append((ore - ooc + ore_robo, clay + clay_robo, obi + obi_robo, geo + geo_robo, ore_robo + 1, clay_robo, obi_robo, geo_robo, t-1))
        # if we can build all robots dont waste time not building
        if check != 15:
            Q.append((ore+ore_robo, clay + clay_robo, obi + obi_robo, geo + geo_robo, ore_robo, clay_robo, obi_robo, geo_robo, t-1))
    return best

with open("Day19.txt") as file:
    lines = file.read().split("\n")

class BluePrint:
    def __init__(self, line):
        parts = line.split(". ")
        self.costs = {"ore": ints(parts[0])[1], "clay": ints(parts[1])[0], "obsidian": ints(parts[2]), "geode": ints(parts[3])}
        self.i = ints(parts[0])[0]

p1 = 0
p2 = 1
for i,line in enumerate(lines):
    bp = BluePrint(line)
    p1 += (i + 1) * solve(bp, 24)
    # first 3 do p2 as well
    if i<3:
        p2 *= solve(bp,32)
print(p1)
print(p2)
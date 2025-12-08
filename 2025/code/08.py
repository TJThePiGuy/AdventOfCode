from aocd.models import Puzzle
from collections import defaultdict
from itertools import combinations
from queue import PriorityQueue

puzzle = Puzzle(year = 2025, day = 8)
data = puzzle.input_data
# data = puzzle.examples[0].input_data

def part_a():
    indexMap = dict()
    for n,line in enumerate(data.split('\n')):
        indexMap[n] = tuple(int(i) for i in line.split(','))
    distQueue = PriorityQueue()
    for (i,p1),(j,p2) in combinations(indexMap.items(), 2):
        dist = sum(abs(a-b)**2 for a,b in zip(p1,p2))
        distQueue.put((dist, (i,j)))

    adjacent = defaultdict(set)
    for _ in range(1000):
        dist, (i,j) = distQueue.get()
        adjacent[i].add(j)
        adjacent[j].add(i)
    
    visited = set()
    sets = []
    for i in indexMap.keys():
        if i in visited:
            continue
        to_visit = set()
        group = set()
        group.add(i)
        to_visit.add(i)
        while(len(to_visit)) > 0:
            next = to_visit.pop()
            if next in visited:
                continue
            visited.add(next)
            group.add(next)
            to_visit = to_visit.union(adjacent[next])
        sets.append(group)
            
    sorts = sorted((len(i) for i in sets), reverse=True)
    ans = sorts[0]*sorts[1]*sorts[2]
    print(ans)
    puzzle.answer_a = ans


def part_b():
    indexMap = dict()
    for n,line in enumerate(data.split('\n')):
        indexMap[n] = tuple(int(i) for i in line.split(','))
    distQueue = PriorityQueue()
    for (i,p1),(j,p2) in combinations(indexMap.items(), 2):
        dist = sum(abs(a-b)**2 for a,b in zip(p1,p2))
        distQueue.put((dist, (i,j)))

    start = True
    adjacent = defaultdict(set)
    visited = set()
    while start or len(visited) != len(indexMap):

        dist, (i,j) = distQueue.get()
        if start:
            visited.add(i)
            start = False

        adjacent[i].add(j)
        adjacent[j].add(i)

        to_visit = set()

        if i in visited:
            to_visit.add(j)
        if j in visited:
            to_visit.add(i)

        while(len(to_visit)) > 0:
            next = to_visit.pop()
            if next in visited:
                continue
            visited.add(next)
            to_visit = to_visit.union(adjacent[next])
    ans = indexMap[i][0] * indexMap[j][0]
    print(ans)
    puzzle.answer_b = ans


part_a()
part_b()
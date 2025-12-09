from aocd.models import Puzzle
from itertools import combinations
from queue import PriorityQueue
from collections import defaultdict

puzzle = Puzzle(year = 2025, day = 9)

data = puzzle.input_data
def part_a():
    points = set(tuple(int(i) for i in line.split(',')) for line in data.split('\n'))
    maxArea = -1
    for (x1, y1), (x2, y2) in combinations(points, 2):
        maxArea = max(maxArea, (abs(x2-x1)+1)*(abs(y2-y1)+1))
    print(maxArea)
    puzzle.answer_a = maxArea

def part_b():
    reds = list(tuple(int(i) for i in line.split(',')) for line in data.split('\n'))
    ymin = min(j for i,j in reds)
    ymax = max(j for i,j in reds)

    bounds = defaultdict(set)

    down_exits = set()

    for (x1, y1), (x2, y2) in zip(reds, reds[1:] + [reds[0]]):

        if x1 == x2:
            down_exits.add((x1, min(y1,y2)))
            for y in range(min(y1,y2),max(y1,y2)+1):
                bounds[y].add(x1)
        else:
            for x in range(min(x1,x2),max(x1,x2)+1):
                bounds[y1].add(x)
    y_ints = defaultdict(set)

    areaQueue = PriorityQueue()

    for (x1, y1), (x2, y2) in (combinations(reds, 2)):
        area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
        areaQueue.put((-area, (x1, y1, x2, y2)))

    for y in (range(ymin, ymax+1)):
        inside = False
        redstop = False
        xl = None
        ints = set()
        for x in sorted(bounds[y]):
            if (x,y) not in reds:
                if redstop:
                    continue
                if inside:
                    ints.add((xl, x))
                    xl = None
                else:
                    xl = x
                inside = not inside
            else:
                if xl is not None:
                    ints.add((xl, x))
                if not redstop:
                    xl = x
                    redstop = True
                else:
                    ints.add((xl, x))
                    if ((xl, y) in down_exits) != ((x, y) in down_exits):
                        inside = not inside
                    if not inside:
                        xl = None
                    else:
                        xl = x
                    redstop = False
        idx = 0
        ints = sorted(set(ints), key=lambda x: x[0])
        while idx < len(ints)-1:
            if ints[idx][1] == ints[idx+1][0]:
                l, _ = ints.pop(idx)
                _,r = ints.pop(idx)
                ints.insert(idx, (l,r))
            else:
                idx += 1
        y_ints[y] = set(ints)


    iters = 0
    while not areaQueue.empty():
        iters += 1
        negArea, (x1, y1, x2, y2) = areaQueue.get()
        xl = min(x1, x2)
        xr = max(x1, x2)
        colorful = True
        for y in range(min(y1,y2),max(y1,y2)+1):
            int_set = y_ints[y]
            found = False
            for L, R in int_set:
                if L<=xl and xr <=R:
                    found = True
                    break
            if not found:
                colorful = False
                break
        if colorful:
            print(-negArea, iters)
            puzzle.answer_b = -negArea
            return
part_a()
part_b()

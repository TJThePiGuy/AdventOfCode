from helper.aocdUtil import getData, submit

rawData = getData(18, 2023)
directions: list[list[str]] = [_.split() for _ in rawData.split("\n")]

dirMap = {3: (0, -1), 0: (1, 0), 1: (0, 1), 2: (-1, 0)}

onPath: list = []

lineArea = 0

x = y = 0

for line in directions:
    dir, dist, color = line

    dir = int(color[-2])
    dist = int(color[2:-2], base=16)

    dx, dy = dirMap[dir]
    x += dx * dist
    y += dy * dist
    if dx < 0:
        lineArea += dist
    elif dy < 0:
        lineArea += dist
    onPath.append((x, y))

innerArea = 0

onPath.append(onPath[0])
for pt1, pt2 in zip(onPath[:-1], onPath[1:]):
    x1, y1 = pt1
    x2, y2 = pt2
    innerArea += (y1 + y2) * (x1 - x2)

submit(int(innerArea / 2 + lineArea) + 1, 18, 2023, "b")
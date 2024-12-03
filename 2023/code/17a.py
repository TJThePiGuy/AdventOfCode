from helper.aocdUtil import getData, submit
from queue import PriorityQueue
from functools import cache

rawData = getData(17, 2023, False)

heatMaps = [[int(_) for _ in line] for line in rawData.split("\n")]
width = len(heatMaps[0])
height = len(heatMaps)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


@cache
def inX(x):
    return x in range(width)


@cache
def inY(y):
    return y in range(height)


positionsToConsider: PriorityQueue = PriorityQueue()
visited: set = set()

positionsToConsider.put((0, (0, 0, 0, 1, [])))
positionsToConsider.put((0, (1, 0, 0, 1, [])))

while not positionsToConsider.empty():
    position = positionsToConsider.get()
    heat, pos = position
    stack: list = []
    d, x, y, forward, stack = pos

    if ((d, x, y, forward)) in visited:
        continue
    visited.add(((d, x, y, forward)))

    if x == width - 1 and y == height - 1:
        finalHeat = heat
        finalStack = stack
        finalStack.append((x, y))
        break

    if forward < 3:
        dx, dy = dirs[d]
        if inX(x + dx) and inY(y + dy):
            newX = x + dx
            newY = y + dy
            newStack = stack.copy()
            newStack.append((x, y))
            positionsToConsider.put(
                (heat + heatMaps[newY][newX], (d, newX, newY, forward + 1, newStack))
            )

    d1 = (d + 1) % 4
    dx, dy = dirs[d1]
    if inX(x + dx) and inY(y + dy):
        newX = x + dx
        newY = y + dy
        newStack = stack.copy()
        newStack.append((x, y))
        positionsToConsider.put(
            (heat + heatMaps[newY][newX], (d1, newX, newY, 1, newStack))
        )

    d2 = (d - 1) % 4
    dx, dy = dirs[d2]
    if inX(x + dx) and inY(y + dy):
        newX = x + dx
        newY = y + dy
        newStack = stack.copy()
        newStack.append((x, y))
        positionsToConsider.put(
            (heat + heatMaps[newY][newX], (d2, newX, newY, 1, newStack))
        )


# for y in range(height):
#     for x in range(width):
#         if (x, y) in finalStack:
#             print("*", end="")
#         else:
#             print(".", end="")
#     print()

print(finalHeat)
submit(finalHeat, 17, 2023, "a")
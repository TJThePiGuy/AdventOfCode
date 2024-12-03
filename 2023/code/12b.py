import helper.aocdUtil as util

solved: dict[tuple[str, str], int] = dict()


def solve(line: str, groups: str, inBlock: bool = False):
    if solved.get((line, groups), -1) != -1:
        return solved[(line, groups)]

    if len(groups) == 0:
        solved[line, groups] = int(line.count("#") == 0)
        return solved[line, groups]

    groupLists = [int(i) for i in groups.split(",")]

    if sum(groupLists) == 0:
        solved[line, groups] = int(line.count("#") == 0)
        return solved[line, groups]

    if len(line) == 0:
        solved[line, groups] = int(sum(groupLists) == 0)
        return solved[line, groups]

    solved[(line, groups)] = 0

    subline = line[1:]
    startChar = line[0]

    if startChar == ".":
        newGroups = groupLists.copy()

        if not inBlock:
            solved[(line, groups)] = solve(
                subline, ",".join([str(i) for i in newGroups]), False
            )
        elif newGroups[0] == 0:
            newGroups.pop(0)
            solved[(line, groups)] = solve(
                subline, ",".join([str(i) for i in newGroups]), False
            )

        return solved[(line, groups)]

    if startChar == "#":
        newGroups = groupLists.copy()

        if not inBlock or newGroups[0] != 0:
            newGroups[0] = newGroups[0] - 1

            solved[(line, groups)] = solve(
                subline, ",".join(str(i) for i in newGroups), True
            )
        return solved[(line, groups)]

    canWhite = canBlack = True

    if groupLists[0] != 0:
        if inBlock:
            canWhite = False
            if line[0] == ".":
                return solved[(line, groups)]

    elif inBlock:
        canBlack = False
        if line[0] == "#":
            return solved[(line, groups)]

    pSum1 = pSum2 = 0

    if canWhite:
        newGroups = groupLists.copy()
        if newGroups[0] == 0:
            newGroups.pop(0)
        pSum1 = solve(subline, ",".join(str(_) for _ in newGroups), False)

    if canBlack:
        newGroups = groupLists.copy()
        newGroups[0] = newGroups[0] - 1
        pSum2 = solve(subline, ",".join(str(_) for _ in newGroups), True)

    solved[(line, groups)] = pSum1 + pSum2
    return solved[(line, groups)]


rawData = util.getData(12, 2023, False)

data = [i.split() for i in rawData.split("\n")]

totalArrange = 0

for x, Line in enumerate(data):
    solved.clear()
    line: str = "?".join([Line[0] for _ in range(5)])
    groups = ",".join([Line[1] for _ in range(5)])
    totalArrange += solve(line, groups)

util.submit(totalArrange, 12, 2023, "b")

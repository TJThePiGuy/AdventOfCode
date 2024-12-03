from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 12, year = 2017)

def part_a():
    data = puzzle.input_data.split('\n')
    # data = '0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5'.split('\n')
    lines = [_.split(' <-> ') for _ in data]
    connect_dict:dict[int,set[int]] = dict()

    for line in lines:
        source = int(line[0])
        targets = set(int(_) for _ in line[1].split(', '))
        connect_dict[source] = targets

    to_check:set[int] = set()
    to_check.add(0)
    checked:set[int] = set()

    connected:set[int] = set()

    while(len(to_check) != 0):
        val = to_check.pop()
        if(val in checked):
            continue
        connected.add(val)
        checked.add(val)
        for new_val in connect_dict[val]:
            if (new_val in checked):
                continue
            to_check.add(new_val)
    
    ans = len(connected)
    puzzle.answer_a = ans
    print(ans)
    

def part_b():
    data = puzzle.input_data.split('\n')
    lines = [_.split(' <-> ') for _ in data]
    connect_dict:dict[int,set[int]] = dict()

    for line in lines:
        source = int(line[0])
        targets = set(int(_) for _ in line[1].split(', '))
        connect_dict[source] = targets

    groups:list[set[int]] = []

    for i in range(len(lines)):
        found = False
        for S in groups:
            if i in S:
                found = True
                break
        if found:
            continue
        
        to_check:set[int] = set()
        to_check.add(i)
        checked:set[int] = set()

        connected:set[int] = set()


        while(len(to_check) != 0):
            val = to_check.pop()
            if(val in checked):
                continue
            connected.add(val)
            checked.add(val)
            for new_val in connect_dict[val]:
                if (new_val in checked):
                    continue
                to_check.add(new_val)
        
        groups.append(connected)
    ans = len(groups)
    puzzle.answer_b = ans
    print(ans)
    

part_a()
part_b()
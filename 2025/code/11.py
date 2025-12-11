from aocd.models import Puzzle
from collections import defaultdict

puzzle = Puzzle(year = 2025, day = 11)

data = puzzle.input_data
# data = puzzle.examples[0].input_data


def part_a():

    descendants = dict()
    def get_descendants(key:str):
        if key in descendants:
            return descendants[key]
        D = children[key].copy()
        for child in children[key]:
            D.update(get_descendants(child))
        descendants[key] = D
        return D
    


    lines = data.split('\n')
    parents = dict()
    children = defaultdict(set)

    for line in lines:
        names = line.split(' ')
        source = names[0][:-1]
        targets = set(names[1:])
        children[source] = targets
        for target in targets:
            if target not in parents:
                parents[target] = set()
            parents[target].add(source)

    valid_keys = get_descendants("you")
    valid_keys.add("you")
    for key in valid_keys:
        children[key].intersection_update(valid_keys)
        if key in parents:
            parents[key].intersection_update(valid_keys)

    paths = defaultdict(int)
    to_visit = set()
    to_visit.add('you')
    paths['you'] = 1
    visited = set()

    while 'out' not in visited:
        curr = to_visit.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for child in children[curr]:
            paths[child] += paths[curr]
            if child not in visited and parents[child] <= visited:
                to_visit.add(child)
    print(paths['out'])
    puzzle.answer_a = paths['out']


def part_b():
    lines = data.split('\n')
    parents:dict[str,set[str]] = dict()
    children = defaultdict(set)
    
    allNames = set()

    for line in lines:
        names = line.split(' ')
        source = names[0][:-1]
        allNames.add(source)
        targets = set(names[1:])
        children[source] = targets
        for target in targets:
            if target not in parents:
                parents[target] = set()
            allNames.add(target)
            parents[target].add(source)

    

    start = True
    to_remove = set()
    while start or len(to_remove) > 0:
        start = False
        to_remove = set()
        for parent in allNames:
            if parent != 'svr' and (parent not in parents or len(parents[parent]) == 0):
                to_remove.add(parent)
                if parent in parents:
                    parents.pop(parent)
                
        allNames.difference_update(to_remove)
        for parent in parents:
            parents[parent].difference_update(to_remove)

    
    
    to_visit = set()
    to_visit.add('svr')
    paths = defaultdict(int)
    paths['svr'] = 1
    visited = set()

    while 'fft' not in visited:
        curr = to_visit.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for child in children[curr]:
            paths[child] += paths[curr]
            if child not in visited and parents[child] <= visited:
                to_visit.add(child)
    
    descendants = dict()
    def get_descendants(key:str):
        if key in descendants:
            return descendants[key]
        D = children[key].copy()
        for child in children[key]:
            D.update(get_descendants(child))
        descendants[key] = D
        return D
    
    valid_keys = get_descendants("fft")
    valid_keys.add("fft")
    for key in valid_keys:
        children[key].intersection_update(valid_keys)
        if key in parents:
            parents[key].intersection_update(valid_keys)

    fftpaths = paths['fft']
    
    to_visit = set()
    to_visit.add('fft')
    paths = defaultdict(int)
    paths['fft'] = fftpaths
    visited = set()


    while 'dac' not in visited:
        curr = to_visit.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for child in children[curr]:
            paths[child] += paths[curr]
            if child not in visited and parents[child] <= visited:
                to_visit.add(child)

    valid_keys = get_descendants("dac")
    valid_keys.add("dac")
    for key in valid_keys:
        children[key].intersection_update(valid_keys)
        if key in parents:
            parents[key].intersection_update(valid_keys)

    
    dacpaths = (paths['dac'])

    to_visit = set()
    to_visit.add('dac')
    paths = defaultdict(int)
    paths['dac'] = dacpaths
    visited = set()

    while 'out' not in visited:
        curr = to_visit.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for child in children[curr]:
            paths[child] += paths[curr]
            if child not in visited and parents[child] <= visited:
                to_visit.add(child)
    ans = paths['out']
    print(ans)
    puzzle.answer_b = ans
part_a()
part_b()
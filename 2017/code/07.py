from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 7, year = 2017)

weights:dict[str,int] = dict()
targets:dict[str,set[str]] = dict()
cum_weights:dict[str,int] = dict()

lines = puzzle.input_data.split("\n")
rules = [line.split(" -> ") for line in lines]

all_targets = set()
sources = set()
for rule in rules:
    startData = rule[0].split()
    source = startData[0]
    val = int(startData[1][1:-1])
    weights[source] = val

    sources.add(source)
    if(len(rule) > 1):
        target_ata = rule[1].split(", ")
        targets[source] = set(target_ata)
        for target in target_ata:
            all_targets.add(target)
    else:
        targets[source] = set()

def get_total_weight(node):
    if node in cum_weights.keys():
        return cum_weights[node]
    total = weights[node]
    for child in targets[node]:
        total += get_total_weight(child)
    cum_weights[node] = total
    return total

def recursive_check(node, GOAL = None):
    children = targets[node]

    if len(children) == 0:
        return((node,GOAL))
    
    different_weights:dict[int,set[str]] = dict()
    for child in children:
        weight = get_total_weight(child)
        if not(weight in different_weights.keys()):
            different_weights[weight] = set()
        different_weights[weight].add(child)
    
    if len(different_weights.keys()) == 1:
        return((node,GOAL - cum_weights[node] + weights[node]))
    keys = list(different_weights.keys())
    key_1 = keys[0]
    key_2 = keys[1]
    if len(different_weights[key_1]) == 1:
        return recursive_check(node = different_weights[key_1].pop(),
                               GOAL = key_2)
    else:
        return recursive_check(node = different_weights[key_2].pop(),
                               GOAL = key_1)

def part_a():
    for source in sources:
        if not(source in all_targets):

            puzzle.answer_a = source
            print(source)
            return(source)
    
def part_b(root):
    goal = recursive_check(root)
    puzzle.answer_b = goal[0]
    print(goal)

root = part_a()
part_b(root)
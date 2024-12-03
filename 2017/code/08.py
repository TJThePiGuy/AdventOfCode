from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 8, year = 2017)

values:dict[str,int] = dict()

def change_val(reg:str, adj:str, val:int):
    if (values.get(reg, 0) == 0):
        values[reg] = 0
    if (adj == 'inc'):
        values[reg] += val
    else:
        values[reg] -= val

def check_cond(reg:str, cond:str, val:int):
    reg_val = values.get(reg, 0)
    if(cond == '=='):
        return reg_val == val
    if(cond == '!='):
        return reg_val != val
    if(cond == '>'):
        return reg_val > val
    if(cond == '>='):
        return reg_val >= val
    if(cond == '<'):
        return reg_val < val
    return reg_val <= val

def part_a():
    data = puzzle.input_data
    rules = [_.split() for _ in data.split('\n')]
    for rule in rules:
        check_reg = rule[4]
        cond = rule[5]
        check_val = int(rule[6])
        if(check_cond(check_reg, cond, check_val)):
            targ_reg = rule[0]
            adj = rule[1]
            targ_val = int(rule[2])
            change_val(targ_reg, adj, targ_val)
    largest = max(values.values())
    puzzle.answer_a = largest
    print(largest)


def part_b():
    data = puzzle.input_data
    rules = [_.split() for _ in data.split('\n')]
    largest = 0
    for rule in rules:
        check_reg = rule[4]
        cond = rule[5]
        check_val = int(rule[6])
        if(check_cond(check_reg, cond, check_val)):
            targ_reg = rule[0]
            adj = rule[1]
            targ_val = int(rule[2])
            change_val(targ_reg, adj, targ_val)
            largest = max(values[targ_reg], largest)
    puzzle.answer_b = largest
    print(largest)


part_a()
values:dict[str,int] = dict()
part_b()
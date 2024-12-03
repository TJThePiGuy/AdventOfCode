from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(day=23, year = 2017)

def part_a():

    data = puzzle.input_data
    rules = [_.split() for _ in data.split('\n')]

    regs:dict[str,int] = dict()

    def get_val(key):
        try:
            val = int(key)
        except:
            val = regs.get(key, 0)
        return(val)

    def set_val(key, val):
        regs[key] = get_val(val)

    muls = 0

    rule_idx = 0

    while(rule_idx < len(rules)):
        rule = rules[rule_idx]
        instr = rule[0]
        if(instr == 'set'):
            set_val(rule[1], rule[2])
        elif(instr == 'sub'):
            val_1 = get_val(rule[1])
            val_2 = get_val(rule[2])
            set_val(rule[1], val_1-val_2)
        elif(instr == 'mul'):
            muls += 1
            val_1 = get_val(rule[1])
            val_2 = get_val(rule[2])
            set_val(rule[1], val_1*val_2)
        elif(instr == 'jnz'):
            val_1 = get_val(rule[1])
            if(val_1 != 0):
                rule_idx += get_val(rule[2])-1
        rule_idx += 1
    
    print(muls)
    puzzle.answer_a = muls

part_a()

def part_b():

    data = puzzle.input_data
    rules = [_.split() for _ in data.split('\n')]
    outstr = ''

    for idx, rule in enumerate(rules):
        outstr = outstr + str(idx) + ' ' + ' '.join(rule) + '\n'

    with open('output', 'w+') as f:
        f.write(outstr)

    h = 0

    for n in range(0, 1001):
        b = 108400 + 17*n
        for d in range(2, b+1):
            if (b/d == b//d and b > d):
                break
        else:
            continue
        h += 1
    print(h)
    puzzle.answer_b = h


part_b()
from aocd.models import Puzzle

puzzle = Puzzle(day=18, year = 2017)

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

    freq = 0

    rule_idx = 0
    while(rule_idx < len(rules)):
        rule = rules[rule_idx]
        instr = rule[0]
        if(instr == 'snd'):
            freq = get_val(rule[1])
        elif(instr == 'set'):
            set_val(rule[1], rule[2])
        elif(instr == 'add'):
            val_1 = get_val(rule[1])
            val_2 = get_val(rule[2])
            set_val(rule[1], val_1+val_2)
        elif(instr == 'mul'):
            val_1 = get_val(rule[1])
            val_2 = get_val(rule[2])
            set_val(rule[1], val_1*val_2)
        elif(instr == 'mod'):
            val_1 = get_val(rule[1])
            val_2 = get_val(rule[2])
            set_val(rule[1], val_1 % val_2)
        elif(instr == 'rcv'):
            val_1 = get_val(rule[1])
            if(val_1) != 0:
                break
        elif(instr == 'jgz'):
            val_1 = get_val(rule[1])
            if(val_1 > 0):
                rule_idx += get_val(rule[2])-1
        rule_idx += 1
    puzzle.answer_a = freq
    print(freq)


def part_b():
    data = puzzle.input_data
    rules = [_.split() for _ in data.split('\n')]

    regs:list[dict[str,int]] = [dict(), dict()]

    def get_val(ind, key):
        try:
            val = int(key)
        except:
            val = regs[ind].get(key, 0)
        return(val)

    def set_val(ind, key, val):
        regs[ind][key] = get_val(ind, val)

    set_val(0, 'p', 0)
    set_val(1, 'p', 1)

    curr_instr = [0,0]
    send_queues = [[],[]]

    is_good = [True, True]
    sends = [0,0]
    curr_prog = 0
    while(any(is_good)):
        while(is_good[curr_prog]):
            rule = rules[curr_instr[curr_prog]]
            instr = rule[0]
            if(instr == 'snd'):
                send_queues[1-curr_prog].insert(0, get_val(curr_prog, rule[1]))
                sends[curr_prog] += 1
                curr_instr[curr_prog] += 1
            elif(instr == 'set'):
                set_val(curr_prog, rule[1], rule[2])
                curr_instr[curr_prog] += 1
            elif(instr == 'add'):
                val_1 = get_val(curr_prog, rule[1])
                val_2 = get_val(curr_prog, rule[2])
                set_val(curr_prog, rule[1], val_1+val_2)
                curr_instr[curr_prog] += 1
            elif(instr == 'mul'):
                val_1 = get_val(curr_prog, rule[1])
                val_2 = get_val(curr_prog, rule[2])
                set_val(curr_prog, rule[1], val_1*val_2)
                curr_instr[curr_prog] += 1
            elif(instr == 'mod'):
                val_1 = get_val(curr_prog, rule[1])
                val_2 = get_val(curr_prog, rule[2])
                set_val(curr_prog, rule[1], val_1 % val_2)
                curr_instr[curr_prog] += 1
            elif(instr == 'rcv'):
                if(len(send_queues[curr_prog]) == 0):
                    is_good[curr_prog] = False
                    break
                val_1 = send_queues[curr_prog].pop()
                set_val(curr_prog, rule[1], val_1)
                curr_instr[curr_prog] += 1
            elif(instr == 'jgz'):
                val_1 = get_val(curr_prog, rule[1])
                if(val_1 > 0):
                    curr_instr[curr_prog] += get_val(curr_prog, rule[2])-1
                curr_instr[curr_prog] += 1
        
        if(len(send_queues[1-curr_prog]) > 0):
            is_good[1-curr_prog] = True
        curr_prog = 1-curr_prog
    puzzle.answer_b = sends[1]
    
    print(sends[1])

part_a()
part_b()
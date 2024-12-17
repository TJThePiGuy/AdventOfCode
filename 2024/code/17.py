from aocd.models import Puzzle
import regex as re

puzzle = Puzzle(day = 17, year = 2024)

data = puzzle.input_data

regs:dict[int,int] = dict() 
registers = re.findall("\\d+", data.split('\n\n')[0])
for i in range(len(registers)):
    regs[i] = int(registers[i])

program = [int(i) for i in re.findall(r'\d+', data.split('\n\n')[1])]
def set_reg(key, val):
    regs[key] = val

def get_combo(idx):
    num = program[idx]
    if num < 4:
        return num
    return regs[num-4]

def part_a():
    idx = 0
    output = ""
    while(idx < len(program)):
        opcode = program[idx]
        idx += 1
        if opcode == 0:
            set_reg(0, regs[0] // (1 << get_combo(idx)))
            idx += 1
        elif opcode == 1:
            set_reg(1, regs[1] ^ program[idx])
            idx += 1
        elif opcode == 2:
            set_reg(1, get_combo(idx) % 8)
            idx += 1
        elif opcode == 3:
            if regs[0] == 0:
                idx += 1
            else:
                idx = program[idx]
        elif opcode == 4:
            set_reg(1, regs[1] ^ regs[2])
            idx += 1
        elif opcode == 5:
            val = get_combo(idx) % 8
            idx += 1
            output = output + ","+str(val)
        elif opcode == 6: 
            set_reg(1, regs[0] // (1 << get_combo(idx)))
            idx += 1
        elif opcode == 7:
            set_reg(2, regs[0] // (1 << get_combo(idx)))
            idx += 1    
    print(output)
    puzzle.answer_a = output[1:]

def part_b():
    worked = {0}
    for correct in range(1,17):
        next_worked = set()
        for item in worked:
            for d in range(8):
                start_A = 8*item + d
                set_reg(0, start_A)
                set_reg(1, 0)
                set_reg(2, 0)
                idx = 0
                val = None
                while val == None:
                    opcode = program[idx]
                    idx += 1
                    if opcode == 0:
                        set_reg(0, regs[0] // (1 << get_combo(idx)))
                        idx += 1
                    elif opcode == 1:
                        set_reg(1, regs[1] ^ program[idx])
                        idx += 1
                    elif opcode == 2:
                        set_reg(1, get_combo(idx) % 8)
                        idx += 1
                    elif opcode == 3:
                        if regs[0] == 0:
                            idx += 1
                        else:
                            idx = program[idx]
                    elif opcode == 4:
                        set_reg(1, regs[1] ^ regs[2])
                        idx += 1
                    elif opcode == 5:
                        val = get_combo(idx) % 8
                        break
                    elif opcode == 6: 
                        set_reg(1, regs[0] // (1 << get_combo(idx)))
                        idx += 1
                    elif opcode == 7:
                        set_reg(2, regs[0] // (1 << get_combo(idx)))
                        idx += 1
                if val == program[-correct]:
                    next_worked.add(start_A)
        worked = next_worked.copy()

    print(min(worked))
    puzzle.answer_b = min(worked)

def hardcoded_b():
    worked = {0}
    for correct in range(1,17):
        next_worked = set()
        for item in worked:
            for d in range(8):
                start_A = 8*item + d
                B = (start_A % 8)
                B = B ^ 7
                C = start_A//(2**B)
                B = B ^ 7
                B = B ^ C
                if B%8 == program[-correct]:
                    next_worked.add(start_A)
        worked = next_worked.copy()
    print(min(worked))
    puzzle.answer_b = min(worked)
part_a()
part_b()
hardcoded_b()
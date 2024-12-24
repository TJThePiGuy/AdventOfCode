from aocd.models import Puzzle

puzzle = Puzzle(year = 2024, day = 24)

data:str = puzzle.input_data
given = [tuple(line.split(': ')) for line in data.split('\n\n')[0].split('\n')]
needed = list(list(line.split(' ')) for line in data.split('\n\n')[1].split('\n'))

vals:dict[str, int] = dict()

for a,b in given:
    vals[a] = int(b)

ops:list[tuple[tuple[str,str], str, str]] = list()

for N in needed:
    ins = tuple(sorted(N[0:3:2]))
    op = N[1]
    res = N[4]
    ops.append((ins, op, res))

def get_z():
    s_vals = sorted(vals, reverse= True)
    z = 0
    for key in s_vals:
        if key[0] == 'z':
            z <<= 1
            z += vals[key]
        else:
            break
    return z

def part_a():
    to_compute = ops.copy()
    while len(to_compute) > 0:
        next_compute = set()
        for (i1,i2),op,res in to_compute:
            if i1 not in vals or i2 not in vals:
                next_compute.add(((i1,i2),op,res))
                continue
            if op == 'OR':
                vals[res] = vals[i1] | vals[i2]
            elif op == 'AND':
                vals[res] = vals[i1] & vals[i2]
            else:
                vals[res] = vals[i1] ^ vals[i2]
        to_compute = next_compute.copy()
    bin = get_z()
    print(bin)
    puzzle.answer_a = bin

digits = 45

def find_str(reg1, reg2, op):
    for ins, o, out in ops:
        if o != op:
            continue
        if (reg1, reg2) != ins and (reg2, reg1) != ins:
            continue
        return out

def swap(str1, str2):
    idx1 = idx2 = -1
    i = 0
    while idx1 == -1 or idx2 == -1:
        _, _, out = ops[i]
        if out == str1:
            idx1 = i
        elif out == str2:
            idx2 = i
        i += 1
    I1, O1, _ = ops[idx1]
    I2, O2, _ = ops[idx2]
    ops[idx1] = (I1, O1, str2)
    ops[idx2] = (I2, O2, str1)

def part_b():
    swap('z07', 'rts')
    swap('z12', 'jpj')
    swap('z26', 'kgj')
    swap('chv', 'vvw')

    carry:dict[int,str] = dict()
    x_xor_y:dict[int,str] = dict()
    x_and_y:dict[int,str] = dict()
    xor_in:dict[int,str] = dict()
    and_in:dict[int,str] = dict()

    for i in range(digits):
        s = str(i)
        if i < 10:
            s = '0'+s
        xstr = 'x'+s
        ystr = 'y'+s
        
        xor_op = find_str(xstr, ystr, 'XOR')
        x_xor_y[i] = xor_op

        if (i == 0):
            carry_str = find_str(xstr, ystr, 'AND')
            x_and_y[i] = carry_str
            carry[i] = carry_str
            continue

        and_str = find_str(xstr, ystr, 'AND')
        x_and_y[i] = and_str

        prev_carry = carry[i-1]
        xor_in_str = find_str(xor_op, prev_carry, 'XOR')
        xor_in[i] = xor_in_str

        and_in_str = find_str(xor_op, prev_carry, 'AND')
        and_in[i] = and_in_str

        carry_str = find_str(and_in_str, and_str, 'OR')
        carry[i] = carry_str
        
    # for I in range(1,digits):
    #     print(I, x_xor_y[I], x_and_y[I], xor_in[I], and_in[I], carry[I])

    swaps = ['z07', 'rts','z12', 'jpj','z26', 'kgj','chv', 'vvw']

    ans = ','.join(sorted(swaps))
    print(ans)
    puzzle.answer_b = ans

def part_b_general():

    carry:dict[int,str] = dict()
    x_xor_y:dict[int,str] = dict()
    x_and_y:dict[int,str] = dict()
    xor_in:dict[int,str] = dict()
    and_in:dict[int,str] = dict()

    swaps:set[str] = set()

    for i in range(digits):
        s = str(i)
        if i < 10:
            s = '0'+s
        xstr = 'x'+s
        ystr = 'y'+s
        zstr = 'z'+s

        xor_str = find_str(xstr, ystr, 'XOR')

        if (i == 0) and xor_str != zstr:
            swaps.add(zstr)
            swaps.add(xor_str)
            swap(zstr, xor_str)
            xor_str = find_str(xstr, ystr, 'XOR')

        x_xor_y[i] = xor_str

        if (i == 0):
            carry_str = find_str(xstr, ystr, 'AND')
            x_and_y[i] = carry_str
            carry[i] = carry_str
            continue

        and_str = find_str(xstr, ystr, 'AND')
        x_and_y[i] = and_str

        prev_carry = carry[i-1]
        xor_in_str = find_str(xor_str, prev_carry, 'XOR')

        if xor_in_str == None:
            swap(xor_str, and_str)
            swaps.add(xor_str)
            swaps.add(and_str)
            xor_str = find_str(xstr, ystr, 'XOR')
            x_xor_y[i] = xor_str
            and_str = find_str(xstr, ystr, 'AND')
            x_and_y[i] = and_str
            xor_in_str = find_str(xor_str, prev_carry, 'XOR')

        if xor_in_str != zstr:
            swap(xor_in_str, zstr)
            swaps.add(xor_in_str)
            swaps.add(zstr)
            xor_str = find_str(xstr, ystr, 'XOR')
            x_xor_y[i] = xor_str
            and_str = find_str(xstr, ystr, 'AND')
            x_and_y[i] = and_str
            xor_in_str = find_str(xor_str, prev_carry, 'XOR')

        xor_in[i] = xor_in_str

        and_in_str = find_str(xor_str, prev_carry, 'AND')
        and_in[i] = and_in_str

        carry_str = find_str(and_in_str, and_str, 'OR')

        carry[i] = carry_str
        
    # for I in range(1,digits):
    #     print(I, x_xor_y[I], x_and_y[I], xor_in[I], and_in[I], carry[I])

    ans = ','.join(sorted(swaps))
    print(ans)
    puzzle.answer_b = ans

part_a()

original = ops.copy()
part_b()

ops = original.copy()
part_b_general()
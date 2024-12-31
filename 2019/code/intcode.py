from collections import defaultdict

def execute_intcode(in_list, RETURN = False):

    instr = defaultdict(int)

    for idx, n in enumerate(in_list):
        instr[idx] = n

    def set_val(idx, val):
        instr[instr[idx]] = val

    def get_val(param, idx):
        if param == 0:
            return instr[instr[idx]]
        return instr[idx]
    
    IDX = 0

    while True:
        opcode = instr[IDX]
        op = opcode % 100
        if op == 99:
            break
        params = opcode // 100

        if op == 1:
            val1 = get_val(params % 10, IDX + 1)
            params //= 10
            val2 = get_val(params % 10, IDX + 2)
            params //= 10
            set_val(IDX+3, val1 + val2)
            IDX += 4
            
        if op == 2:
            val1 = get_val(params % 10, IDX + 1)
            params //= 10
            val2 = get_val(params % 10, IDX + 2)
            params //= 10
            set_val(IDX+3, val1 * val2)
            IDX += 4
  
        if op == 3:
            IN = int(input("Enter INPUT: "))
            set_val(IDX + 1, IN)
            IDX += 2
        
        if op == 4:
            print(get_val(params % 10, IDX + 1))
            IDX += 2

        if op == 5:
            if get_val(params % 10, IDX+1) != 0:
                params //= 10
                IDX = get_val(params % 10, IDX + 2)
            else:
                IDX += 3

        if op == 6:
            if get_val(params % 10, IDX+1) == 0:
                params //= 10
                IDX = get_val(params % 10, IDX + 2)
            else:
                IDX += 3

        if op == 7:
            val1 = val1 = get_val(params % 10, IDX + 1)
            params //= 10
            val2 = get_val(params % 10, IDX + 2)
            params //= 10
            set_val(IDX+3, 1 if val1 < val2 else 0)
            IDX += 4
            
        if op == 8:
            val1 = val1 = get_val(params % 10, IDX + 1)
            params //= 10
            val2 = get_val(params % 10, IDX + 2)
            params //= 10
            set_val(IDX+3, 1 if val1 == val2 else 0)
            IDX += 4
    if RETURN:
        return get_val(1, 0)
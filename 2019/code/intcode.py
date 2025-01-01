from collections import defaultdict

class IntCodeComputer:

    def __init__(self, instructions, return_first = False, print_out = True, input_console = True, input_arr = [], start_idx = 0):
        self.rel_base = 0
        self.instr = defaultdict(int)

        for idx, n in enumerate(instructions):
            self.instr[idx] = n
        self.return_first = return_first
        self.print_out = print_out
        self.input_console = input_console
        self.input_arr = input_arr.copy()
        self.output_arr = []
        self.idx = start_idx
        self.finished = False

    def set_val(self, param, idx, val):
        if param == 0:
            self.instr[self.instr[idx]] = val
        if param == 2:
            self.instr[self.get_val(1, idx) + self.rel_base] = val

    def get_val(self, param, idx):
        if param == 0:
            return self.instr[self.instr[idx]]
        if param == 1:
            return self.instr[idx]
        if param == 2:
            return self.instr[self.get_val(1, idx) + self.rel_base]

    def add_input(self, inp):
        self.input_arr.append(inp)

    def compute(self):
        ct = 0
        while True:
            opcode = self.instr[self.idx]
            op = opcode % 100
            if op == 99:
                self.finished = True
                break
            params = opcode // 100
            if op == 1:
                val1 = self.get_val(params % 10, self.idx + 1)
                params //= 10
                val2 = self.get_val(params % 10, self.idx + 2)
                params //= 10
                self.set_val(params % 10, self.idx+3, val1 + val2)
                self.idx += 4
                
            if op == 2:
                val1 = self.get_val(params % 10, self.idx + 1)
                params //= 10
                val2 = self.get_val(params % 10, self.idx + 2)
                params //= 10
                self.set_val(params % 10, self.idx+3, val1 * val2)
                self.idx += 4
    
            if op == 3:
                if self.input_console:
                    IN = int(input("Enter INPUT: "))
                else:
                    if len(self.input_arr) == 0:
                        return
                    IN = self.input_arr.pop(0)
                self.set_val(params % 10, self.idx + 1, IN)
                self.idx += 2
            
            if op == 4:
                if self.print_out:
                    print(self.get_val(params % 10, self.idx + 1))
                self.output_arr.append(self.get_val(params % 10, self.idx + 1))
                # print(len(self.output_arr))
                self.idx += 2

            if op == 5:
                if self.get_val(params % 10, self.idx+1) != 0:
                    params //= 10
                    self.idx = self.get_val(params % 10, self.idx + 2)
                else:
                    self.idx += 3

            if op == 6:
                if self.get_val(params % 10, self.idx+1) == 0:
                    params //= 10
                    self.idx = self.get_val(params % 10, self.idx + 2)
                else:
                    self.idx += 3

            if op == 7:
                val1 = self.get_val(params % 10, self.idx + 1)
                params //= 10
                val2 = self.get_val(params % 10, self.idx + 2)
                params //= 10
                self.set_val(params % 10, self.idx+3, 1 if val1 < val2 else 0)
                self.idx += 4
                
            if op == 8:
                val1 = self.get_val(params % 10, self.idx + 1)
                params //= 10
                val2 = self.get_val(params % 10, self.idx + 2)
                params //= 10
                self.set_val(params % 10, self.idx+3, 1 if val1 == val2 else 0)
                self.idx += 4

            if op == 9:
                val1 = self.get_val(params % 10, self.idx + 1)
                self.rel_base += val1
                self.idx += 2
            
        if self.return_first:
            return self.get_val(1, 0)


def execute_intcode(in_list, RETURN = False, PRINT = True, CONSOLE_INPUT = True):

    instr = defaultdict(int)

    REL_BASE = 0
    for idx, n in enumerate(in_list):
        instr[idx] = n

    def set_val(param, idx, val):
        if param == 0:
            instr[instr[idx]] = val
        if param == 2:
            instr[get_val(1, idx) + REL_BASE] = val

    def get_val(param, idx):
        if param == 0:
            return instr[instr[idx]]
        if param == 1:
            return instr[idx]
        if param == 2:
            return instr[get_val(1, idx) + REL_BASE]
    
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
            set_val(params % 10, IDX+3, val1 + val2)
            IDX += 4
            
        if op == 2:
            val1 = get_val(params % 10, IDX + 1)
            params //= 10
            val2 = get_val(params % 10, IDX + 2)
            params //= 10
            set_val(params % 10, IDX+3, val1 * val2)
            IDX += 4
  
        if op == 3:
            IN = int(input("Enter INPUT: "))
            set_val(params % 10, IDX + 1, IN)
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
            val1 = get_val(params % 10, IDX + 1)
            params //= 10
            val2 = get_val(params % 10, IDX + 2)
            params //= 10
            set_val(params % 10, IDX+3, 1 if val1 < val2 else 0)
            IDX += 4
            
        if op == 8:
            val1 = get_val(params % 10, IDX + 1)
            params //= 10
            val2 = get_val(params % 10, IDX + 2)
            params //= 10
            set_val(params % 10, IDX+3, 1 if val1 == val2 else 0)
            IDX += 4

        if op == 9:
            val1 = get_val(params % 10, IDX + 1)
            REL_BASE += val1
            IDX += 2
        
    if RETURN:
        return get_val(1, 0)
from aocd.models import Puzzle

puzzle = Puzzle(day=24, year = 2017)

def inds_to_hash(inds):
    return(sum(ind_to_bin(inds)))

def ind_to_bin(ind):
    return 1 << ind

def hash_to_inds(hash):
    S = set()
    i = 0
    while(hash > 0):
        if(hash % 2 == 1):
            S.add(i)
        i += 1
        hash //= 2
    return(S)

def part_a():
    data = puzzle.input_data
    val_map:dict[int,int] = dict()
    ports = list(list(int(i) for i in _.split('/')) for _ in data.split('\n'))
    for idx, p in enumerate(ports):
        for val in p:
            if val not in val_map.keys():
                 val_map[val] = 0
            val_map[val] |= ind_to_bin(idx)
    start_inds = [i for i in range(len(ports)) if 0 in ports[i]]
    largest_length = 0
    bridges_to_check:set[tuple[int, int, int]] = set()

    largest_left:dict[tuple[int,int,int],int] = dict()

    def get_val(ind:int, val:int, bin_bridge:int) -> int:
        if largest_left.get((ind, val, bin_bridge), "c") != "c":
            return(largest_left[(ind, val, bin_bridge)])
        unused_bit_inds = val_map[val] ^ (val_map[val] & bin_bridge)
        if(unused_bit_inds == 0):
            largest_left[((ind, val, bin_bridge))] = sum(ports[ind])
            return sum(ports[ind])
        largest_subtree = 0
        next_inds = hash_to_inds(unused_bit_inds)
        for new_ind in next_inds:
            new_port = ports[new_ind].copy()
            new_port.remove(val)
            new_val = new_port[0]
            new_bin_bridge = bin_bridge | ind_to_bin(new_ind)
            largest_subtree = max(largest_subtree,
                                  get_val(new_ind, new_val, new_bin_bridge))
        largest_left[(ind, val, bin_bridge)] = sum(ports[ind]) + largest_subtree
        return largest_left[(ind, val, bin_bridge)]
    
    max_length = 0
    for idx in start_inds:
        val = max(ports[idx])
        max_length = max(max_length, get_val(idx, val, ind_to_bin(idx)))
    puzzle.answer_a = max_length
    print(max_length)



def part_b():
    data = puzzle.input_data
    # data = '0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10'

    val_map:dict[int,int] = dict()
    ports = list(list(int(i) for i in _.split('/')) for _ in data.split('\n'))
    for idx, p in enumerate(ports):
        for val in p:
            if val not in val_map.keys():
                 val_map[val] = 0
            val_map[val] |= ind_to_bin(idx)
    start_inds = [i for i in range(len(ports)) if 0 in ports[i]]
    largest_length = 0
    bridges_to_check:set[tuple[int, int, int]] = set()

    largest_left:dict[tuple[int,int,int],tuple[int,int]] = dict()

    def get_val(ind:int, val:int, bin_bridge:int) -> tuple[int,int]:
        if largest_left.get((ind, val, bin_bridge), "c") != "c":
            return(largest_left[(ind, val, bin_bridge)])
        unused_bit_inds = val_map[val] ^ (val_map[val] & bin_bridge)

        if(unused_bit_inds == 0):
            largest_left[((ind, val, bin_bridge))] = (1, sum(ports[ind]))
            return((1, sum(ports[ind])))
        
        longest_subtree = 0
        best_subtree = 0

        next_inds = hash_to_inds(unused_bit_inds)
        for new_ind in next_inds:
            new_port = ports[new_ind].copy()
            new_port.remove(val)
            new_val = new_port[0]
            new_bin_bridge = bin_bridge | ind_to_bin(new_ind)
            subtree_data = get_val(new_ind, new_val, new_bin_bridge)
            sub_length, sub_strength = subtree_data
            if(sub_length > longest_subtree):
                longest_subtree = sub_length
                best_subtree = sub_strength
            elif(sub_length == longest_subtree and sub_strength >= best_subtree):
                longest_subtree = sub_length
                best_subtree = sub_strength

        largest_left[(ind, val, bin_bridge)] = (1 + longest_subtree, sum(ports[ind]) + best_subtree)
        return largest_left[(ind, val, bin_bridge)]
    
    max_L = 0
    max_S = 0
    for ind in start_inds:
        data = get_val(ind, max(ports[ind]), ind_to_bin(ind))
        if(max_L < data[0]) or (max_L == data[0] and max_S < data[1]):
            max_L = data[0]
            max_S = data[1]
    print(max_L, max_S)
    puzzle.answer_b = max_S

part_a()

part_b()
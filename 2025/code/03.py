from aocd.models import Puzzle

puzzle = Puzzle(year = 2025, day = 3)

data = puzzle.input_data
# data = puzzle.examples[0].input_data

def part_a():
    total = 0
    for line in data.split():
        m = -1
        for n, i in enumerate(line):
            for j in line[n+1:]:
                m = max(m, int(i+j))
        total += m
    print(total)
    puzzle.answer_a = total


def part_b():
    total = 0
    for line in data.split():
        L = len(line)
        m = -1
        partition = []
        for n, i in enumerate(line):
            for k, j in enumerate(line[n+1:], n+1):
                if int(i+j) > m:
                    partition = [-1, n,k, L]
                    m = max(m, int(i+j))
        best_prev = m
        # print(partition, best_prev)

        for sublen in range(3,13):
            curr_best = -1
            best_prev_str = str(best_prev)
            for place, (start_idx, end_idx) in enumerate(zip(partition[:-1], partition[1:])):
                for idx, next_elem in enumerate(line[start_idx+1:end_idx], start_idx+1):
                    test_num = int(best_prev_str[:place] + next_elem + best_prev_str[place:])
                    if curr_best < test_num:
                        best_partition = partition[:place+1] + [idx] + partition[place+1:]
                        curr_best = test_num
            partition = best_partition
            best_prev = curr_best
            # print(partition, curr_best)
        
        # print(curr_best)
        total += curr_best
    print(total)
    puzzle.answer_b = total

part_a()
part_b()
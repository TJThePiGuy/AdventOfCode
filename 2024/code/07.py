from aocd.models import Puzzle

puzzle = Puzzle(day = 7, year = 2024)

def part_a():
    data = puzzle.input_data
    total = 0
    for line in data.split('\n'):
        line = line.split(': ')
        test_val = int(line[0])
        items = [int(i) for i in line[1].split(' ')]
        results = {items[0]}
        for item in items[1:]:
            new_results = set()
            for result in results:
                new_nums = [result + item, result * item]
                for num in new_nums:
                    if num <= test_val:
                        new_results.add(num)
            results = new_results.copy()
        if test_val in results:
            total += test_val
    puzzle.answer_a = total
    print(total)

def part_b():
    data = puzzle.input_data
    total = 0
    for line in data.split('\n'):
        line = line.split(': ')
        test_val = int(line[0])
        items = [int(i) for i in line[1].split(' ')]
        results = {items[0]}
        for item in items[1:]:
            new_results = set()
            for result in results:
                new_nums = [result + item, result * item, int(str(result) + str(item))]
                for num in new_nums:
                    if num <= test_val:
                        new_results.add(num)
            results = new_results.copy()
        if test_val in results:
            total += test_val
    puzzle.answer_b = total
    print(total)

part_a()
part_b()    
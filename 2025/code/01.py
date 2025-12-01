from aocd.models import Puzzle

puzzle = Puzzle(year = 2025, day = 1)

data = puzzle.input_data

def part_a():
    dir = data.split()
    zeros=  0
    pos = 50
    for d in dir:
        if d[0] == "R":
            pos += int(d[1:])
        else:
            pos -= int(d[1:])
        if pos % 100 == 0:
            zeros += 1
        # print(pos)
    print(zeros)
    puzzle.answer_a = zeros
    
def part_b():
    dir = data.split()
    zeros=  0
    pos = 50
    prev_pos = 50
    for d in dir:
        dist = int(d[1:])
        zerosThisTime = 0
        if d[0] == "R":
            pos += dist
            zerosThisTime += (pos-prev_pos) // 100
            if prev_pos + (dist%100) >= 100:
                zerosThisTime += 1
        else:
            pos -= dist
            zerosThisTime += (prev_pos - pos) // 100
            if prev_pos !=0 and prev_pos - (dist%100) <= 0:
                zerosThisTime += 1
        # print(d, prev_pos, pos, zerosThisTime)
        pos %= 100
        prev_pos = pos
        zeros += zerosThisTime
    print(zeros)
    puzzle.answer_b = zeros
    
part_a()
part_b()
from aocd.models import Puzzle
from collections import defaultdict

puzzle = Puzzle(year = 2025, day = 7)

data = puzzle.input_data

def part_a():
    sx = -1
    splitters = defaultdict(set)
    for y,line in enumerate(data.split('\n')):
        for x,chr in enumerate(line):
            if chr == "S":
                sx = x
            elif chr == '^':
                splitters[y].add(x)
    beams = set()
    beams.add(sx)
    splits = 0
    for y,line in enumerate(data.split('\n')[1:],1):
        newBeams = set()
        for beam in beams:
            if beam in splitters[y]:
                newBeams.add(beam-1)
                newBeams.add(beam+1)
                splits += 1
            else:
                newBeams.add(beam)
        beams = newBeams.copy()
    print(splits)
    puzzle.answer_a = splits

def part_b():
    sx = -1
    splitters = defaultdict(set)
    for y,line in enumerate(data.split('\n')):
        for x,chr in enumerate(line):
            if chr == "S":
                sx = x
            elif chr == '^':
                splitters[y].add(x)
    beams = defaultdict(int)
    beams[sx] = 1
    for y,line in enumerate(data.split('\n')[1:],1):
        newBeams = defaultdict(int)
        for beam, count in beams.items():
            if beam in splitters[y]:
                newBeams[beam+1] += count
                newBeams[beam-1] += count
            else:
                newBeams[beam] += count
        beams = newBeams.copy()
    print(sum(beams.values()))
    puzzle.answer_b = sum(beams.values())

part_a()

part_b()
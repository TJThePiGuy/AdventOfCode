from aocd.models import Puzzle
import regex as re

puzzle = Puzzle(day = 4, year = 2024)

def part_a():

    data = puzzle.input_data
    lines = data.split('\n')
    W = len(lines[0])
    H = len(lines)
    X_S = set()
    for y in range(H):
        for x in range(W):
            if lines[y][x] == 'X':
                X_S.add((x,y))
    M_S = set()
    for pt in X_S:
        x,y = pt
        for dx in [-1,0,1]:
            if x+dx in [-1,W]:
                continue
            for dy in [-1,0,1]:
                if y+dy in [-1,H]:
                    continue
                if lines[y+dy][x+dx] == 'M':
                    M_S.add((x+dx,y+dy,dx,dy))
    A_S = set()
    for pt in M_S:
        x,y,dx,dy = pt
        if x+dx in [-1,W]:
            continue
        if y+dy in [-1,H]:
            continue
        if lines[y+dy][x+dx] == 'A':
            A_S.add((x+dx,y+dy,dx,dy))

    TOT = 0
    for pt in A_S:
        x,y,dx,dy = pt
        if x+dx in [-1,W]:
            continue
        if y+dy in [-1,H]:
            continue
        if lines[y+dy][x+dx] == 'S':
            TOT += 1
    print(TOT)
    puzzle.answer_a = TOT



def part_b():
    data = puzzle.input_data

    lines = data.split('\n')
    A_S = set()
    W = len(lines[0])
    H = len(lines)
    line = data.replace('\n','')
    for x in range(len(line)):
        if x < W:
            continue
        if x >= W*(H-1):
            continue
        if (x % H) == 0:
            continue
        if (x % H) == H-1:
            continue
        if line[x]=='A':
            A_S.add(x)
    TOT = 0
    for x in A_S:
        down_l = line[x-(W+1):x+(W+1)+1:W+1]
        down_r = line[x-(W-1):x+(W-1)+1:W-1]
        if down_r in ['MAS', 'SAM'] and down_l in ['MAS', 'SAM']:
            TOT += 1

    print(TOT)
    puzzle.answer_b = TOT

part_a()
part_b()
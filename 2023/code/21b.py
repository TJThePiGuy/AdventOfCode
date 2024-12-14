from aocd.models import Puzzle
from tqdm import tqdm
import numpy as np

puzzle = Puzzle(day = 21, year = 2023)

dirs = {(1,0),(-1,0),(0,1),(0,-1)}

data = puzzle.input_data
data = puzzle.examples[0].input_data
# data = '...S...'

grid = data.split('\n')
height = len(grid)
width = len(grid[0])
boulders:set[int] = set()

start_pos = -1

for y in range(height):
    for x in range(width):
        if grid[y][x] == 'S':
            start_pos = y*width + x
        elif grid[y][x] == '#':
            boulders.add(y*width + x)

trans_mat = np.zeros((width*height, width*height))

for coord in range(width*height):
    if coord in boulders:
        continue
    total = 4
    for delta in [-1,1,-width,width]:
        if delta == -1 and coord % width == 0:
            continue
        if delta == 1 and (coord + 1) % width == 0:
            continue
        if delta == -width and coord < width:
            continue
        if delta == width and coord >= height*(width-1):
            continue
        neighbor = (coord + delta) % (width*height)
        if neighbor in boulders:
            continue
        trans_mat[neighbor, coord] = 1

start = np.zeros((width*height, 1))
start[start_pos] = 1

print(trans_mat)

total_trans_mat = np.linalg.matrix_power(trans_mat, 1)

total_effect = np.multiply(total_trans_mat, start)
print(len(np.nonzero(total_effect)))
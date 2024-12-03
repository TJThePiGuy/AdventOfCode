# AOC 2024 Day 1

Happy AOC!

## Part A

Strong start to day 1, mixed up how I was sorting my columns, but besides that, I felt it was pretty easy. Finished #970 in the world, which I'll take for not being as prepared as I wanted to be.

## Part B

Sure, O(n^2) isn't exactly the best, but it was quck here. Being #631 in the world was good, though. Can't wait for the rest of em!

## Code

```python
import regex
from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2024, day=1)

def part_a():

    data = puzzle.input_data.split('\n')

    rows = [_.split() for _ in data]
    col1 = sorted([int(rows[j][0]) for j in range(len(rows))])
    col2 = sorted([int(rows[j][1]) for j in range(len(rows))])

    diff = [abs(col1[i] - col2[i]) for i in range(len(col1))]

    puzzle.answer_a = sum(diff)
    print(sum(diff))

def part_b():
    data = puzzle.input_data.split('\n')

    rows = [_.split() for _ in data]
    col1 = sorted([int(rows[j][0]) for j in range(len(rows))])
    col2 = sorted([int(rows[j][1]) for j in range(len(rows))])
    total = 0
    for j in col1:
        for i in col2:
            if i==j:
                total += i
    puzzle.answer_b = total
    print(total)

part_a()
part_b()
```
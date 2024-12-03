from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 4, year = 2017)

def part_a():
    phrases = [_.split() for _ in puzzle.input_data.split("\n")]
    count = 0
    for phrase in phrases:
        seen = set()
        for word in phrase:
            if word in seen:
                break
            seen.add(word)
        else:
            count = count + 1
    puzzle.answer_a = count
    print(count)

def part_b():
    phrases = [_.split() for _ in puzzle.input_data.split("\n")]
    count = 0
    for phrase in phrases:
        good = True
        for idx, word1 in enumerate(phrase):
            s_word1 = sorted(word1)
            for word2 in phrase[idx+1:]:
                if(good and sorted(word2) == s_word1):
                    good = False
            if not(good):
                break
        if(good):
            count += 1
    puzzle.answer_b = count
    print(count)

part_a()
part_b()
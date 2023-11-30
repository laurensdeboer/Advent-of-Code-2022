import re

def partOne() -> int:
    with open ("input.txt") as file:
        pairs = file.read().strip().split('\n')

    count = 0
    pattern = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

    for pair in pairs:
        match = re.match(pattern, pair)
        a, b, c, d = map(int, match.groups())
        if ((a >= c and b <= d) or (a <= c and b >= d)):
            count += 1

    return count

def partTwo() -> int:
    with open ("input.txt") as file:
        pairs = file.read().strip().split('\n')

    count = 0
    pattern = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

    for pair in pairs:
        match = re.match(pattern, pair)
        a, b, c, d = map(int, match.groups())
        if (a <= d and b >= c):
            count += 1

    return count

answerPartOne = partOne()
print(f"Answer part one: {answerPartOne}")
answerPartTwo = partTwo()
print(f"Answer part two: {answerPartTwo}")
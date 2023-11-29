def getPriority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1 
    else:
        return ord(item) - ord('A') + 27

def partOne() -> int:
    with open("input.txt") as file:
        rucksacks = file.read().strip().split('\n')

    prioritySum = 0

    for rucksack in rucksacks:
        mid = (len(rucksack) // 2)
        commonItem = set(rucksack[mid:]) & set(rucksack[:mid])
        prioritySum += getPriority(commonItem.pop())

    return prioritySum

def main():
    answerPartOne = partOne()
    print(f"Part 1 answer: {answerPartOne}")

if __name__ == '__main__':
    main()
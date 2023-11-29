def partOne() -> int:
    topCalories = 0
    currentCalories = 0

    with open("input.txt") as file:
        for line in file:
            if line != '\n':
                currentCalories += int(line.strip())

            elif line == '\n':
                if (currentCalories > topCalories):
                    topCalories = currentCalories
                currentCalories = 0

    return topCalories

def partTwo() -> int:
    currentCalories = 0
    topThreeCalories = []
    result = 0

    with open("input.txt") as file:
        for line in file:
            if line != '\n':
                currentCalories += int(line.strip())

            elif line == '\n':
                topThreeCalories.append(currentCalories)
                currentCalories = 0

        topThreeCalories.append(currentCalories)
        
    topThreeCalories.sort(reverse=True)

    for i in range(3):
        result += topThreeCalories[i]

    return result

if __name__ == '__main__':
    answer = partTwo()
    print(answer)
cyclesToCalculate = [20, 60, 100, 140, 180, 220]

def calculateSignalStrength(currentCycles: int, xReg: int) -> int:
    for cycle in cyclesToCalculate:
        if currentCycles == cycle:
            return currentCycles * xReg
    return 0

def partOne() -> int:
    x = 1
    cycles = 0
    result = 0

    fileName = "input.txt"
    file = open(fileName)

    for line in file:
        values = line.split()
        if values[0] == "noop":
            cycles += 1
            result += calculateSignalStrength(cycles, x)

        elif values[0] == "addx":
            for i in range(2):
                cycles += 1
                result += calculateSignalStrength(cycles, x)

            x += int(values[1])

    file.close()
    return result

def main():
    answer = partOne()
    print(answer)

if __name__ == '__main__':
    main()
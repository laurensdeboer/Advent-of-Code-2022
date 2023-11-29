def partOne():
    scoreMap = {'A': {'X': 3, 'Y': 6, 'Z': 0},
                'B': {'X': 0, 'Y': 3, 'Z': 6},
                'C': {'X': 6, 'Y': 0, 'Z': 3}}

    shapeMap = {'X': 1, 'Y': 2, 'Z': 3}

    totalScore = 0

    with open("input.txt") as file:
        for line in file:
            opponent, you = line.strip().split()
            outcomeScore = scoreMap[opponent][you]
            shapeScore = shapeMap[you]
            totalScore += (outcomeScore + shapeScore)

    return totalScore

def partTwo():
    shapeMap = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
                'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
                'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}

    roundScoreMap = {'X': 0, 'Y': 3, 'Z': 6}
    shapeScoreMap = {'X': 1, 'Y': 2, 'Z': 3}

    totalScore = 0

    with open("input.txt") as file:
        for line in file:
            opponent, outcome = line.strip().split()
            shapeToChoose = shapeMap[opponent][outcome]
            roundScore = roundScoreMap[outcome]
            shapeScore = shapeScoreMap[shapeToChoose]
            totalScore += (roundScore + shapeScore)

    return totalScore

def main():
    answer = partTwo()
    print(answer)

if __name__ == '__main__':
    main()

# X = Lose
# Y = Draw
# Z = Win

# A Y     
# Opponent chooses ROCK
# It must become DRAW
# You must choose ROCK

# B X
# Opponent chooses PAPER
# You must LOSE
# You must chooose ROCK

# C Z
# Opponent chooses SCISSORS 
# You must WIN
# You must choose ROCK
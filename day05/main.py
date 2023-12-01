import re

def partOne():
    # Initialize a 2d array with three stacks
    stacks = [[] for _ in range(3)]
    
    with open ("temp.txt") as file:
        crates, moves = file.read().split("\n\n")

    print(crates.split())

partOne()

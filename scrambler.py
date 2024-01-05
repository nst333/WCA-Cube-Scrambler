import os
import sys
import random

modes = 0

def showModes():
     global modes

     print("Square Cubes")
     print("\t[2] 2x2x2")
     print("\t[3] 3x3x3")
     print("\t[4] 4x4x4")
     print("\t[5] 5x5x5")
     print("\t[6] 6x6x6")
     print("\t[7] 7x7x7")
     print()

     print("Special Cubes")
     print("\t[8] Megaminx")
     print("\t[9] Pyraminx")
     print("\t[10] Square-1")
     print("\t[11] Skewb")

     print("\t[99] Exit")
     print()

     modes = int(input("Select Modes : "))

showModes()

squareScramble = [
        'R', 'L', 'U', 'D', 'F', 'B'
]

result = []

# cube's layer - 1 = modes

if modes == 99:
    sys.exit(0)
elif modes == 2:
    
    for _ in range(10):
        cscramble = random.choice(squareScramble)
        if random.choice([0,1]) == 0: # Select is prime move
            cscramble += "'"
        elif random.choice([0,1]) == 0: # Select is twice move
            cscramble += "2"
        result.append(cscramble)
elif modes == 3:

    for _ in range(15):
        cscramble = random.choice(squareScramble)
        if random.choice([0,1]) == 0:
            cscramble += "'"
        elif random.choice([0,1]) == 0:
            cscramble += "2"
        result.append(cscramble)
elif modes == 4:

    for _ in range(20):
        cscramble = random.choice(squareScramble)
        if random.choice([0,1]) == 0:
            cscramble += "w"
        if random.choice([0,1]) == 0:
            cscramble += "'"
        elif random.choice([0,1]) == 0:
            cscramble += "2"
        result.append(cscramble)
elif modes == 5:

    for _ in range(25):
        cscramble = random.choice(squareScramble)
        if random.choice([0,1]) == 0:
            cscramble += "w"
        if random.choice([0,1]) == 0:
            cscramble += "'"
        elif random.choice([0,1]) == 0:
            cscramble += "2"
        result.append(cscramble)
elif modes == 6:

    for _ in range(30):
        cscramble = random.choice(squareScramble)
        if random.choice([0,1]) == 0:
            cscramble = "3" + cscramble
        if random.choice([0,1]) == 0:
            cscramble += "w"
        if random.choice([0,1]) == 0:
            cscramble += "'"
        elif random.choice([0,1]) == 0:
            cscramble += "2"
        result.append(cscramble)
elif modes == 7:

    for _ in range(35):
        cscramble = random.choice(squareScramble)
        if random.choice([0,1]) == 0:
            cscramble = "3" + cscramble
        if random.choice([0,1]) == 0:
            cscramble += "w"
        if random.choice([0,1]) == 0:
            cscramble += "'"
        elif random.choice([0,1]) == 0:
            cscramble += "2"
        result.append(cscramble)
elif modes == 8:
    scrambleList = [
        "R++", "R--", "D++", "D--", "U", "U'"
    ]

    for _ in range(77):
        cscramble = random.choice(scrambleList)
        result.append(cscramble)
elif modes == 9:
    scrambleList = [
        'R', 'B', 'L', 'U', 'r', 'b', 'l', 'u'
    ]

    for _ in range(10):
        cscramble = random.choice(scrambleList)
        if random.choice([0,1]) == 0:
            cscramble += "'"
        elif random.choice([0,1]) == 0:
            cscramble += "2"
        result.append(cscramble)
elif modes == 10:
    scrambleList = [
        '0','1','2','3','4','5','6'
    ]

    for _ in range(16):
        # Create single set
        tempR = []
        for _ in range(2):
            cscramble = random.choice(scrambleList)
            if random.choice([0,1]) == 0:
                cscramble += "-"
            tempR.append(cscramble)
        result.append(f"({tempR[0]},{tempR[1]})/")
elif modes == 11:
    scrambleList = [
        'R','U','B','L'
    ]

    for _ in range(10):
        cscramble = random.choice(scrambleList)
        if random.choice([0,1]) == 0:
            cscramble += "'"
        elif random.choice([0,1]) == 0:
            cscramble += "2"
        result.append(cscramble)

os.system('cls')
print("Scramble")

for r in result:
    print(r, end=' ')
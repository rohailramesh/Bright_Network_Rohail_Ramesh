import queue

#This function creates the maze
def createFloor():
    floor = []
    floor.append(["-", "-", "-", "-", "-", "-", "O", "-", "-", "-"])
    floor.append([" ", " ", " ", " ", " ", "", " ", " ", " ", " "])
    floor.append([" ", " ", " ", "#", " ", "#", " ", " ", " ", " "])
    floor.append([" ", " ", "#", " ", " ", " ", " ", " ", " ", " "])
    floor.append([" ", " ", " ", "#", " ", " ", " ", " ", " ", " "])
    floor.append([" ", "#", " ", " ", " ", " ", " ", " ", " ", " "])
    floor.append([" ", "#", " ", "#", " ", "#", " ", " ", " ", " "])
    floor.append([" ", " ", " ", " ", " ", " ", " ", "#", "#", "#"])
    floor.append([" ", " ", "#", " ", " ", " ", " ", " ", " ", " "])
    floor.append([" ", " ", " ", "#", " ", "#", "#", " ", " ", "X"])

    return floor

#This function prints the maze
def printMaze(floor, path=""):
    for x, pos in enumerate(floor[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(floor):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


#This function checks if the move is valid or not
def valid(floor, moves):
    for x, pos in enumerate(floor[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(floor[0]) and 0 <= j < len(floor)):
            return False
        elif (floor[j][i] == "#"):
            return False

    return True


#This function finds the path from the start point to the end point
def findEnd(floor, moves):
    for x, pos in enumerate(floor[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if floor[j][i] == "X":
        print("Found: " + moves)
        printMaze(floor, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
floor = createFloor()

while not findEnd(floor, add):
    add = nums.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(floor, put):
            nums.put(put)
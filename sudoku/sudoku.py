import board as b
import sys


print("Enter values of board as a string of just numbers, use 0 for empty spaces")
values = input()
while len(values) != 81:
    print("Length of string is not 81, try again? (y/n)")
    answer = input()
    if answer == "y":
        print("Enter values of board as a string of just numbers, use 0 for empty spaces")
        values = input()
    else:
        sys.exit()

theBoard = []
successes = []
#Initialize custom groupings each row, column and 3x3 box in a sudoku puzzle
col1, col2, col3, col4, col5, col6, col7, col8, col9 = b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9)))
row1, row2, row3, row4, row5, row6, row7, row8, row9 = b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9)))
box1, box2, box3, box4, box5, box6, box7, box8, box9 = b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9))),b.groups([],set((1,2,3,4,5,6,7,8,9)))

cols = [col1, col2, col3, col4, col5, col6, col7, col8, col9]
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9] #3x3 boxes in a sudoku grid
allGroups = [col1, col2, col3, col4, col5, col6, col7, col8, col9,row1, row2, row3, row4, row5, row6, row7, row8, row9,box1, box2, box3, box4, box5, box6, box7, box8, box9]

def initialize():
    """
    appends each tile to the corresponding groups
    uses r and c as row and column trackers
    """ 
    r,c = 1, 1
    for i in values:
        if c < 9:
            try:
                space = b.tile((c,r), int(i))
                cols[c-1].append(space)
                rows[r-1].append(space)
                boxes[(int((r-1)/3)*3+int((c-1)/3))].append(space)
                if int(i) != 0:
                    successes.append(space)
                else:
                    theBoard.append(space)
                c+=1
            except:
                print("Inputted Sudoku String is not correct Format")
                print("Try again? (y/n)")
                answer = input()
                if answer == "y":
                    for group in allGroups:
                        group.clear()
                    initialize()
                else:
                    sys.exit()
        else:
            try:
                space = b.tile((c,r),int(i))
                cols[c-1].append(space)
                rows[r-1].append(space)
                boxes[(int((r-1)/3)*3+int((c-1)/3))].append(space)
                if int(i) != 0:
                    successes.append(space)
                else:
                    theBoard.append(space)
                c = 1
                r+=1
            except:
                print("Inputted Sudoku String is not correct Format")
                print("Try again? (y/n)")
                answer = input()
                if answer == "y":
                    for group in allGroups:
                        group.clear()
                    initialize()
                else:
                    sys.exit()

def backTrack(tile):
    """
    Sets the value of the node with smallest current domain
    Then appends that node to successes
    And removes it from theBoard (tiles which still do not have a value)

    If a tile cannot have a value set (meaning it has an empty domain or has gone through its domain)
    removes the past node from successes,
    appends it back to theBoard,
    backtracks one step
    resets the domains of all tiles and the 3 groups the backtracked tile belongs to
    calls backTrack again to continue process until a valid path is found
    """
    if tile.setValue() is not False:
        for group in tile.memberOf:
            group.domain.remove(tile.getValue())
        successes.append(tile)
        theBoard.remove(tile)
    else:
        tile.counter = 0
        theBoard.insert(0, successes[len(successes)-1])
        successes.pop(len(successes)-1)
        for group in theBoard[0].memberOf:
            group.domain.add(theBoard[0].getValue())
        for box in theBoard:
            box.updateDomain()
        theBoard.sort(key =lambda t: len(t.domain))
        backTrack(theBoard[0])


initialize() #Initializes board
failure = len(successes)-1 
if len(successes)<81:
    for group in allGroups:
        group.updateDomain()
"""
Initializes the domain of each group based on the values
not found in the tiles of each group
"""

while len(successes)<81:
    """
    Continues using DFS until all 81 tiles have a non-0 value
    If backtracking ever backtracks to a tile that has a default 
    non-0 value, ends program as no solution is found
    Updates the domain of all no-solution tiles after a value is added to a tile
    """
    if len(successes) == failure:
        print("No solution found")
        sys.exit()
    for box in theBoard:
        box.updateDomain()
    theBoard.sort(key =lambda t: len(t.domain))
    backTrack(theBoard[0])

#Print Answer
successes.sort(key = lambda tile: (tile.cord[1], tile.cord[0]))
answer = ""
for tile in successes:
    answer += f" {tile.getValue()}"
print(answer)
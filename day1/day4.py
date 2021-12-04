def readPuzzleInput():
    drawdata = []
    boarddata = []
    with open ('day4puzzleinput.txt', "r") as datafile:
        drawdata = datafile.readline()
        boarddata = [x.strip() for x in datafile.readlines()]
        print(boarddata)
    return drawdata, boarddata

if __name__ == "__main__":
    readPuzzleInput()
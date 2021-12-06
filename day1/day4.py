"""
Part 1:

    The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19

    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7
    After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    Finally, 24 is drawn:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

    The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

    To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Part 2:

    On the other hand, it might be wise to try a different strategy: let the giant squid win.

    You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

    In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

    Figure out which board will win last. Once it wins, what would its final score be?

"""
import numpy as np

def readPuzzleInput():
    drawdata = []
    boardlist = []
    with open ('day4puzzleinput.txt', "r") as datafile:
        drawdata = [int(x) for x in datafile.readline().strip().split(',')] #first line is draw data
        boarddata = [x.strip() for x in datafile.readlines() if x.strip()] # each board is 5 rows of 5 digits seperated by a eol
        for i in range(0,len(boarddata),5):
            boardlines = [[int(y) for y in x.split()] for x in boarddata[i:i+5]]
            boardlist.append(Board(boardlines))
    return drawdata, boardlist

class Board():
    def __init__(self,boardlines):
        self.boardvalues = np.array(boardlines)
        self.xdim, self.ydim = self.boardvalues.shape
        self.boardhits = np.zeros((self.xdim,self.ydim))
        self.numhits = 0
        self.bingo = False
    
    def getValue(self):
        return self.boardvalues.sum()

    def checkBingo(self):
        if not self.bingo:
            if self.numhits >= self.xdim or self.numhits >= self.ydim:
                for row in range(0,self.xdim-1):
                    if self.boardhits[row ,: ].sum() == self.xdim:
                        self.bingo = True
                for column in range(0,self.ydim-1):
                    if self.boardhits[ :,column].sum() == self.ydim:
                        self.bingo = True
        return self.bingo

    def markDraw(self,drawnum):
        x, y = np.where(self.boardvalues == drawnum)
        if x.size > 0 and y.size > 0:
            self.numhits+=1
            self.boardvalues[x,y] = 0
            self.boardhits[x,y] = 1
            self.checkBingo()    
    
    def __str__(self):
        return str(self.boardvalues)

def part1(draw,boardlist):
    bingo = False
    while len(draw) > 0 and not bingo:
        num = draw.pop(0)
        for board in boardlist:
           board.markDraw(num)
           bingo = board.checkBingo()
           if bingo:
               print("Unmarked values on the winning board are;")
               print(board)
               print("Sum of winning board is {}. Drawn number was {}. Total is {}.".format(board.getValue(),num,board.getValue()*num))
               break
               
def part2(draw,boardlist):
    while len(draw) > 0:
        num = draw.pop(0)
        if len(boardlist) > 1:
            for board in boardlist[:]:
                    board.markDraw(num)
                    if board.checkBingo():
                        boardlist.remove(board)    
        else:
            boardlist[0].markDraw(num)
            bingo = boardlist[0].checkBingo()
            if bingo:
                print("Unmarked values on the losing board are;")
                print(boardlist[0])
                print("Sum of losing board is {}. Drawn number was {}. Total is {}.".format(boardlist[0].getValue(),num,boardlist[0].getValue()*num))
                break

if __name__ == "__main__":
    draw, boards = readPuzzleInput()
    print("The answer to part 1 is;")
    part1(draw,boards)
    print("The answer to part 2 is;")
    part2(draw,boards)    
"""
--- Day 13: Transparent Origami ---
Part 1:

    You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

    Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

    Congratulations on your purchase! To activate this infrared thermal imaging
    camera system, please enter the code found on page 1 of the manual.
    Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

    6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5
    The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    ...........
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........
    Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    -----------
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........
    Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

    #.##..#..#.
    #...#......
    ......#...#
    #...#......
    .#.#..#.###
    ...........
    ...........
    Now, only 17 dots are visible.

    Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

    Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

    The second fold instruction is fold along x=5, which indicates this line:

    #.##.|#..#.
    #...#|.....
    .....|#...#
    #...#|.....
    .#.#.|#.###
    .....|.....
    .....|.....
    Because this is a vertical line, fold left:

    #####
    #...#
    #...#
    #...#
    #####
    .....
    .....
    The instructions made a square!

    The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

    How many dots are visible after completing just the first fold instruction on your transparent paper?

Part 2:

    Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

    What code do you use to activate the infrared thermal imaging camera system?
"""
import numpy as np
def readPuzzleInput():
    points = []
    folds = []
    with open("day13puzzleinput.txt", "r") as datafile:
        lines = [x.strip() for x in datafile.readlines() if x.strip() != '']
        points = [tuple([int(y) for y in x.split(',')]) for x in lines if x[0].isdigit()]
        folds = [tuple([y for y in x.split(' ')][2].split('=')) for x in lines if not x[0].isdigit()]
        folds = [(x[0],int(x[1])) for x in folds]

    return(points,folds)

class TransparentPaper():

    def __init__(self,points,folds):
        
        self.folds = folds
        # depending on the data, the folds could be on the fold line or below it. if we use the values
        # for the folds rather than the values of the data we will make sure our array is big enough to 
        # take same sized chunks of grid for purposes of "folding"
        maxX = 2 * (max([x[1] for x in folds if x[0] == 'x'])) + 1 
        maxY = 2 * (max([y[1] for y in folds if y[0] == 'y'])) + 1
        
        self.paper = np.zeros((maxY,maxX),dtype=int)  

        for x,y in points:
            self.paper[y,x] =1
        print("Created a Transparent Paper with the dimensions of {}".format(self.paper.shape))

    def shortenx(self,num):
        print("Folding to the left (x axis) at {}".format(num))
        leftHalf = self.paper[:, :num]
        rightHalf = self.paper[:,2*num:num:-1]
        self.paper = np.add(leftHalf,rightHalf)
        numpoints = np.count_nonzero(self.paper)
        return numpoints


    def shorteny(self,num):
        print("Folding to the top (y axis) at {}".format(num))
        topHalf = self.paper[:num, :]
        bottomHalf = self.paper[2*num:num:-1, : ]
        self.paper = np.add(topHalf,bottomHalf)
        numpoints = np.count_nonzero(self.paper)
        return numpoints

    def fold(self):
        #fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines)
        if self.folds:
            axis,num = self.folds.pop(0)
            if axis == "x": # shorten board on x column by num lines
                numpoints = self.shortenx(num)
            elif axis == "y" : #shorten board on y column by num lines
                numpoints = self.shorteny(num)  
            return numpoints 
        else:
            return -1

    def printGrid(self):
        for y in range(0,self.paper.shape[0]):
            print()
            for x in range(0,self.paper.shape[1]):
                if self.paper[y,x] > 0:
                    print("*",end=' ')
                else:
                    [print(" ",end = ' ')]


def part1():
    points,folds = readPuzzleInput()
    paper = TransparentPaper(points,folds)
    numpoints = paper.fold()
    print("{} total points visible after folding".format(numpoints))

def part2():
    points,folds = readPuzzleInput()
    paper = TransparentPaper(points,folds)
    while paper.fold() != -1:
            pass
    paper.printGrid()

if __name__ == "__main__":
    print("The answer to part 1 is;")
    part1()
    print("The answer for part 2 is;")
    part2()

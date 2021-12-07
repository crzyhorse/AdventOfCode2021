"""
--- Day 5: Hydrothermal Venture ---
Part 1:

    You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

    They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2
    Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
    For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

    So, the horizontal and vertical lines from the above list would produce the following diagram:

    .......1..
    ..1....1..
    ..1....1..
    .......1..
    .112111211
    ..........
    ..........
    ..........
    ..........
    222111....
    In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

    To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

    Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

Part Two:

    Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

    Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
    Considering all lines from the above example would now produce the following diagram:

    1.1....11.
    .111...2..
    ..2.1.111.
    ...1.2.2..
    .112313211
    ...1.2....
    ..1...1...
    .1.....1..
    1.......1.
    222111....
    You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

    Consider all of the lines. At how many points do at least two lines overlap?

"""
import numpy as np
def readPuzzleInput():
    with open("day5puzzleinput.txt", "r") as datafile:
        lines = [x.strip().split("->") for x in datafile.readlines()]
        pointlist = []
        xdim = 0
        ydim = 0
        for pair in lines:
            start, end = pair
            xstart, ystart = start.split(',')
            xend, yend = end.split(',')
            xend=int(xend)
            yend=int(yend)
            xstart=int(xstart)
            ystart=int(ystart)
            if xend > xdim:
                xdim = xend 
            if yend > ydim:
                ydim = yend
            if xstart > xdim:
                xdim = xstart
            if ystart > ydim:
                ydim = ystart
            pointlist.append([(xstart,ystart),(xend,yend)])
        xdim+=1
        ydim+=1
        return xdim,ydim,pointlist

class Grid():

    def drawLines(self,countdiagonal=False):
        for pairs in self.pointlist:
            xstart,ystart = pairs[0]
            xend,yend = pairs[1]
            if xstart == xend:
                self.drawVerticalLines(ystart,yend,xstart)
            elif ystart == yend:
                self.drawHorizontalLines(xstart,xend,ystart)
            else:
                if countdiagonal:
                    self.drawDiagonalLines(xstart,ystart,xend,yend)

        self.calculateIntersections()

    def drawHorizontalLines(self,xstart,xend,ypos):
        if xstart > xend:
            pointrange = range(xstart,xend-1,-1)
        elif xstart < xend:
            pointrange = range(xstart,xend+1,1)
        for xpos in pointrange:
            self.grid[ypos,xpos]+=1

    def drawVerticalLines(self,ystart,yend,xpos):
        if ystart > yend:
            pointrange = range(ystart,yend-1,-1)
        elif ystart < yend:
            pointrange = range(ystart,yend+1,1)
        for ypos in pointrange:
            self.grid[ypos,xpos]+=1
        
    def drawDiagonalLines(self,xstart,ystart,xend,yend):
        xpos = xstart
        ypos = ystart
        if xstart > xend and ystart > yend: # up and left
            while xpos != xend-1 and ypos != yend-1:
                self.grid[ypos,xpos] += 1
                xpos-=1
                ypos-=1
        elif xstart > xend and ystart < yend: # down and left
            while xpos != xend-1 and ypos!= yend+1:
                self.grid[ypos,xpos] += 1
                xpos-=1
                ypos+=1
        elif xstart < xend and ystart > yend: # up and right
            while xpos != xend+1 and ypos!= yend-1:
                self.grid[ypos,xpos] += 1
                xpos+=1
                ypos-=1
        elif xstart < xend and ystart < yend: # down and right
            while xpos != xend+1 and ypos!=yend+1:
                self.grid[ypos,xpos] += 1
                xpos+=1
                ypos+=1
        
    def calculateIntersections(self):
        count = (self.grid > 1).sum()
        print(count)
                    
    def __init__(self,pointlist,xdim,ydim):
        self.pointlist = pointlist
        self.xdim = xdim
        self.ydim = ydim
        self.grid = np.zeros((self.ydim,self.xdim))
        
def part1(xdim,ydim,pointlist):
    grid = Grid(pointlist,xdim,ydim)
    grid.drawLines()

def part2(xdim,ydim,pointlist):
    grid = Grid(pointlist,xdim,ydim)
    grid.drawLines(True)

if __name__ == "__main__":
    xdim, ydim, pointlist = readPuzzleInput()
    part1(xdim,ydim,pointlist)
    part2(xdim,ydim,pointlist)
"""
--- Day 9: Smoke Basin ---

Part 1:
    These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

    If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

    Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

    Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

    In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

    The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

    Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Part 2:
    Next, you need to find the largest basins so you know what areas are most important to avoid.

    A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

    The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

    The top-left basin, size 3:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    The top-right basin, size 9:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    The middle basin, size 14:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    The bottom-right basin, size 9:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

    What do you get if you multiply together the sizes of the three largest basins?
"""
import numpy as np
def readPuzzleInput():
    with open ("day9puzzleinput.txt", "r") as datafile:
        data =[[int(y) for y in x.strip()] for x in datafile.readlines()]
    return data


class Heatmap():
    
    def part1(self):
        print("The risk level of your heatmap is {}".format(self.getRiskLevel()))
        
    def part2(self):
        print("The sizes of the three largest basins multiplied is {}".format(self.getBasins()))
        
    def __init__(self,data):
        self.array = np.array(data)
        self.y,self.x = self.array.shape
        self.lowpoints = []
        self.basins = {}
        self.getLowPoints()
        for lowpoint in self.lowpoints:
            self.basins.setdefault(lowpoint,[])

    def getLowPoints(self):
        for row in range(0,self.y):
            for column in range(0,self.x):
                adjacent = {}
                num = self.array[row,column]
                tocheck = {}
                if row > 0:
                    adjacent['previousrow'] = self.array[row-1,column]
                if row < self.y-1:
                    adjacent['nextrow'] = self.array[row+1,column]
                if column < self.x-1:
                    adjacent['nextcolumn'] = self.array[row,column+1]
                if column > 0:
                    adjacent['previouscolumn'] = self.array[row,column-1]
                lowestcount = 0
                for value in adjacent.values():
                    if num < value:
                        lowestcount += 1
                if lowestcount == len(adjacent.values()):
                    self.lowpoints.append((row,column))
    
    def getBasins(self):
        lens = []
        for lowpoint in self.lowpoints:
            pointobj = {}
            pointobj['coord'] = lowpoint
            pointobj['value'] = self.array[lowpoint]
            self.basins[lowpoint] = self.findPoints([pointobj],[])
            lens.append(len(self.basins[lowpoint]))                
        return np.prod(sorted(lens,reverse=True)[:3])



    def checkWest(self,y,x):
        if x == 0: return [] # cant check west because we are at the boundary
        retList = []
        curx = x-1
        stop = False
        while not stop:
            retdict = {'coord':(), 'value':0}
            value = self.array[y,curx]
            if value != 9:
                retdict['coord'] = (y,curx)
                retdict['value'] = value
                retList.append(retdict)
                if curx > 1:
                    curx-=1
                else:
                    stop = True
            else:
                stop = True
        return retList

    def checkNorth(self,y,x):
        if y == 0: return [] # can't check north because we are at the boundary
        retList = []
        cury = y-1
        stop = False
        while not stop:
            retdict = {'coord':(), 'value':0}
            value = self.array[cury,x]
            if value != 9:
                retdict['coord'] = (cury,x)
                retdict['value'] = value
                retList.append(retdict)
                if cury > 1:
                    cury-=1
                else:
                    stop = True
            else:
                stop = True

        return retList

    def checkEast(self,y,x):
        if x == self.x-1: return [] # can't check east because we are at the boundary
        retList = []
        curx = x+1
        stop = False
        while not stop:
            retdict = {'coord':(), 'value':0}
            value = self.array[y,curx]
            if value != 9:
                retdict['coord'] = (y,curx)
                retdict['value'] = value
                retList.append(retdict)
                if curx < self.x-1:
                    curx+=1
                else:
                    stop = True
            else:
                stop = True
        return retList

    def checkSouth(self,y,x):
        if y == self.y-1: return [] # can't check south because we are at the boundary
        retList = []
        cury = y+1
        stop = False
        while not stop:
            retdict = {'coord':(), 'value':0}
            value = self.array[cury,x]
            if value != 9:
                retdict['coord'] = (cury,x)
                retdict['value'] = value
                retList.append(retdict)
                if cury < self.y-1:
                    cury+=1
                else:
                    stop = True
            else:
                stop = True
        return retList

    def findPoints(self,pointlist,checkedpoints):
        newpointlist = []
        if not pointlist:
            return checkedpoints
        for object in pointlist:
            if object not in checkedpoints:
                y,x = object['coord']
                west = self.checkWest(y,x)
                if west: newpointlist.append(west)
                east= self.checkEast(y,x)
                if east: newpointlist.append(east)
                north = self.checkNorth(y,x)
                if north: newpointlist.append(north)
                south = self.checkSouth(y,x)
                if south: newpointlist.append(south)
                checkedpoints.append(object)
                if newpointlist:
                    flatten =  [item for sublist in newpointlist for item in sublist if item not in checkedpoints]
                    self.findPoints(flatten,checkedpoints)
               
        return checkedpoints

    def getRiskLevel(self):
        risklevel = 0
        for lowpoint in self.lowpoints:
            risklevel += self.array[lowpoint]+1
        return risklevel

if __name__ == "__main__":
    data = readPuzzleInput()
    map = Heatmap(data)
    print("The answer to part 1 is:")
    map.part1()
    print("The answer to part 2 is:")
    map.part2()

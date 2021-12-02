def readPuzzleInput():
    """ 
    copied and pasted text from browser window to puzzleinput.txt file. read it in order into a list of ints.
    """
    data = []
    with open ('day1puzzleinput.txt', "r") as datafile:
        for line in datafile.readlines():
            data.append(int(line))        
    return data

def part1(sonarReadings):
    """
    Find the number of times a depth measurement increases from the previous measurement. 

    Example;
    199 (N/A - no previous measurement)
    200 (increased)
    208 (increased)
    210 (increased)
    200 (decreased)
    207 (increased)
    240 (increased)
    269 (increased)
    260 (decreased)
    263 (increased)
    """
    increase = 0
    decrease = 0
    equal = 0
    previous = None
    for reading in sonarReadings:
        if not previous:
            pass
        elif previous > reading:
            decrease+=1
        elif previous < reading:
            increase+=1
        elif previous == reading:
            equal+=1
        previous = reading
    print("The depth readings increased from previous {} times.".format(increase))
    print("The depth readings decreased from previous {} times.".format(decrease))
    print("The depth readings were equal to previous {} times.".format(equal))

def part2(sonarReadings):
    """
    Find the number of times sums of 3 measure sliding window increases from the previous.
    example;

    199  A      
    200  A B    
    208  A B C  
    210    B C D
    200  E   C D
    207  E F   D
    240  E F G  
    269    F G H
    260      G H
    263        H

    A (199+200+208)
    B (200+208+210)
    etc
    """    
    listOfWindows = []
    for x in range(len(sonarReadings)):
        if (x+2 < len(sonarReadings)):
           listOfWindows.append(sonarReadings[x]+sonarReadings[x+1]+sonarReadings[x+2])
    part1(listOfWindows)


if __name__ == "__main__":
    sonarReadings = readPuzzleInput()
    print("The answers to part 1 are;")
    part1(sonarReadings)
    print("The answers to part 2 are;")
    part2(sonarReadings)
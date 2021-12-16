"""
--- Day 14: Extended Polymerization ---

Part1 

    The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

    The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

    For example:

    NNCB

    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C
    The first line is the polymer template - this is the starting point of the process.

    The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

    So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

    The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
    The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
    The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
    Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

    After the first step of this process, the polymer becomes NCNBCHB.

    Here are the results of a few steps using the above rules:

    Template:     NNCB
    After step 1: NCNBCHB
    After step 2: NBCCNBBBCBHCB
    After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
    After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
    
    This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.
4
7
13
25
49
97
    Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

"""
pairs = {}

def readPuzzleInput(part2=False):
    global pairs
    pairs = {}
    pattern = ""
    with open("day14puzzleinput.txt", "r") as datafile:
        pattern = datafile.readline().strip()
        datafile.readline() # skip blank
        for line in datafile.readlines():
            line = [x.strip() for x in line.split('->')]
            if not part2:
                pairs[line[0]] = line[1]
            else:
                pairs[(ord(line[0][0]),ord(line[0][1]))] = ord(line[1])
    if part2:
        patternList = []
        for x in range(0,len(pattern)-1):
            patternList.append(ord(pattern[x]))
        print(patternList)
        pattern = patternList
    return pattern

def replacePattern(pattern):
    returnPattern = ""
    for x in range(0,len(pattern)-1):
        returnPattern += pattern[x]+pairs[pattern[x:x+2]]
    returnPattern+=pattern[-1]
    return returnPattern

def part1(numtimes):
    pattern = readPuzzleInput()
    # numtimes is leftover from the hopeful thought that i could solve part 2 with the same code LOL 
    x = 0
    while x<numtimes: 
        print("Pass number :{}".format(x+1))  
        pattern = replacePattern(pattern)
        x+=1
    count = {}
    for value in set(pairs.values()):
        count[value] = pattern.count(value)
    most = max([count[x] for x in count.keys()])
    least = min([count[x] for x in count.keys()])
    print("The answer is {}".format(most-least))


if __name__=="__main__":
    print("The answer to part 1 is:")
    part1(10)
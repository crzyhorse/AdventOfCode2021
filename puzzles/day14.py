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
import sys, copy
pairs = {}
lastchar = ""

def stepTest(step, count):
    print("Testing {} with {}".format(step,count))
    if step == 1:
        if not count == {'CH': 1, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 1, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 1, 'NB': 1, 'BN': 0, 'BB': 0, 'BC': 1, 'CC': 0, 'CN': 1}:
            print(count)
            print({'CH': 1, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 1, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 1, 'NB': 1, 'BN': 0, 'BB': 0, 'BC': 1, 'CC': 0, 'CN': 1})
            return False
        else:
            return True
    if step == 2:
        if not count == {'CH': 0, 'HH': 0, 'CB': 2, 'NH': 0, 'HB': 0, 'HC': 1, 'HN': 0, 'NN': 0, 'BH': 1, 'NC': 0, 'NB': 2, 'BN': 0, 'BB': 2, 'BC': 2, 'CC': 1, 'CN': 1}:
            return False
        else:
            return True
    if step == 3:
        if not count == {'CH': 2, 'HH': 1, 'CB': 0, 'NH': 0, 'HB': 3, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 1, 'NC': 1, 'NB': 4, 'BN': 2, 'BB': 4, 'BC': 3, 'CC': 1, 'CN': 2}:
            print({'CH': 2, 'HH': 1, 'CB': 0, 'NH': 0, 'HB': 3, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 1, 'NC': 1, 'NB': 4, 'BN': 2, 'BB': 4, 'BC': 3, 'CC': 1, 'CN': 2})
            return False
        else:
            return True
    if step == 4:
        if not count == {'CH': 0, 'HH': 1, 'CB': 5, 'NH': 1, 'HB': 0, 'HC': 3, 'HN': 1, 'NN': 0, 'BH': 3, 'NC': 1, 'NB': 9, 'BN': 6, 'BB': 9, 'BC': 4, 'CC': 2, 'CN': 3}: 
            return False
        else:
            return True
    return True


def readPuzzleInput(part2=False):
    global pairs
    global lastchar
    pairs = {}
    pattern = ""
    with open("day14test.txt", "r") as datafile:
        pattern = datafile.readline().strip()
        datafile.readline() # skip blank
        for line in datafile.readlines():
            line = [x.strip() for x in line.split('->')]
            pairs[line[0]] = line[1]
    lastchar = pattern[-1]
    if part2:
        patternDict = {}
        for x in range(0,len(pattern)-1):
            patternDict.setdefault(pattern[x]+pattern[x+1],0)
        pattern = patternDict
        
    return pattern

def replacePattern(pattern):
    returnPattern = ""
    for x in range(0,len(pattern)-1):
        returnPattern += pattern[x]+pairs[pattern[x:x+2]]
    returnPattern+=pattern[-1]
    return returnPattern

def part1(numtimes):
    pattern = readPuzzleInput()
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

def printx(chainCount):
    newdict = {}
    for x in [x for x in chainCount.keys() if chainCount[x] > 0]:
        newdict[x] = chainCount[x]
    print(newdict)

def part2(numtimes):
    chainCount = {}
    for pair in pairs.keys():
        chainCount.setdefault(pair,0)
    zeroCount = copy.deepcopy(chainCount)
    pattern = readPuzzleInput(True)
    for combo in pattern.keys():
        chainCount[combo]+=1
    x = 0
    while x<numtimes:
        print("Pass number:{}".format(x+1))
        copyCount = copy.deepcopy(zeroCount)
        print("Copy is {}".format(copyCount))
        for combo in chainCount.keys():
            if chainCount[combo] > 0:
                print("combo removed is {}".format(combo))
                newchar = pairs[combo]
                comb1 = combo[0]+newchar
                comb2 = newchar+combo[1]
                print('Combos added are {} and {}'.format(comb1,comb2))
                copyCount[combo]-= 1
                copyCount[comb1]+= 1
                copyCount[comb2]+= 1
        print("copyvcount is {}".format(copyCount))
        print("chainCount is {}".format(chainCount))
        for key,value in copyCount.items():
            chainCount[key]+=value
        x+=1
        print("Chaincount is {}".format(chainCount))
        if not stepTest(x,chainCount):
            print("Test failed.")
            sys.exit()
        elemDict = {}
        for key in chainCount.keys():
            elemDict.setdefault(key[0],0)
            elemDict[key[0]] += chainCount[key]
        elemDict[lastchar]+=1
        #print(elemDict)
    #print(chainCount)

if __name__=="__main__":
    print("The answer to part 1 is:")
    part1(10)
    part2(10)
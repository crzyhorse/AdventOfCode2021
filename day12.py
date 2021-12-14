"""
Part 1:

    With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

    Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:

    start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end
    This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

    So, the above cave system looks roughly like this:

        start
        /   \
    c--A-----b--d
        \   /
        end
    Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

    Given these rules, there are 10 paths through this example cave system:

    start,A,b,A,c,A,end
    start,A,b,A,end
    start,A,b,end
    start,A,c,A,b,A,end
    start,A,c,A,b,end
    start,A,c,A,end
    start,A,end
    start,b,A,c,A,end
    start,b,A,end
    start,b,end
    (Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

    Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.

    Here is a slightly larger example:

    dc-end
    HN-start
    start-kj
    dc-start
    dc-HN
    LN-dc
    HN-end
    kj-sa
    kj-HN
    kj-dc
    The 19 paths through it are as follows:

    start,HN,dc,HN,end
    start,HN,dc,HN,kj,HN,end
    start,HN,dc,end
    start,HN,dc,kj,HN,end
    start,HN,end
    start,HN,kj,HN,dc,HN,end
    start,HN,kj,HN,dc,end
    start,HN,kj,HN,end
    start,HN,kj,dc,HN,end
    start,HN,kj,dc,end
    start,dc,HN,end
    start,dc,HN,kj,HN,end
    start,dc,end
    start,dc,kj,HN,end
    start,kj,HN,dc,HN,end
    start,kj,HN,dc,end
    start,kj,HN,end
    start,kj,dc,HN,end
    start,kj,dc,end
    Finally, this even larger example has 226 paths through it:

    fs-end
    he-DX
    fs-he
    start-DX
    pj-DX
    end-zg
    zg-sl
    zg-pj
    pj-he
    RW-he
    fs-DX
    pj-RW
    zg-RW
    start-pj
    he-WI
    zg-he
    pj-fs
    start-RW
    How many paths through this cave system are there that visit small caves at most once?
Part 2:
    After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

    Now, the 36 possible paths through the first example above are:

    start,A,b,A,b,A,c,A,end
    start,A,b,A,b,A,end
    start,A,b,A,b,end
    start,A,b,A,c,A,b,A,end
    start,A,b,A,c,A,b,end
    start,A,b,A,c,A,c,A,end
    start,A,b,A,c,A,end
    start,A,b,A,end
    start,A,b,d,b,A,c,A,end
    start,A,b,d,b,A,end
    start,A,b,d,b,end
    start,A,b,end
    start,A,c,A,b,A,b,A,end
    start,A,c,A,b,A,b,end
    start,A,c,A,b,A,c,A,end
    start,A,c,A,b,A,end
    start,A,c,A,b,d,b,A,end
    start,A,c,A,b,d,b,end
    start,A,c,A,b,end
    start,A,c,A,c,A,b,A,end
    start,A,c,A,c,A,b,end
    start,A,c,A,c,A,end
    start,A,c,A,end
    start,A,end
    start,b,A,b,A,c,A,end
    start,b,A,b,A,end
    start,b,A,b,end
    start,b,A,c,A,b,A,end
    start,b,A,c,A,b,end
    start,b,A,c,A,c,A,end
    start,b,A,c,A,end
    start,b,A,end
    start,b,d,b,A,c,A,end
    start,b,d,b,A,end
    start,b,d,b,end
    start,b,end
    The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.

    Given these new rules, how many paths through this cave system are there?
"""
def readPuzzleInput():
    data = []
    with open ("day12puzzleinput.txt", "r") as datafile:
        data = [x.strip() for x in datafile.readlines()]
    return data

caves = {}

def caveSize(cavename):
    if cavename.lower() == cavename:
        return 'small'
    else:
        return 'large'

def buildCaves(data):
    for line in data:
        cavename, connectedcavename = line.split('-')
        if cavename not in caves.keys():
            caves.setdefault(cavename,[])
            if connectedcavename!='start' and cavename != 'end':
                caves[cavename].append(connectedcavename)
        else:
            if cavename != 'end':
                if connectedcavename not in caves[cavename]:
                    if connectedcavename != 'start':
                        caves[cavename].append(connectedcavename)

        if connectedcavename not in caves.keys():
            caves.setdefault(connectedcavename,[]) 
            if cavename != 'start' and connectedcavename!='end':
                caves[connectedcavename].append(cavename)
        else:   
            if connectedcavename != 'end':
                if cavename not in caves[connectedcavename]:
                    if cavename != 'start':
                        caves[connectedcavename].append(cavename)
    return caves

def part1(data):
    global caves 
    caves = buildCaves(data)
    del(caves['end'])
    for cave in list(caves.keys()): # remove deadends - cave with only one link and they are both lowercase
        if cave.lower() == cave and cave.lower()!='start':
            if len(caves[cave]) ==1:
                if caves[cave][0].upper() != caves[cave][0]:
                    removecave = caves[cave][0]
                    caves[removecave].remove(cave)
                    del(caves[cave])

    print("Our caves are")
    print(caves)
    combos = navigateTo('start',[])
    print("We found {} paths.".format(len(combos)))


def navigateTo(node,visited):
    global caves
    visited = visited + [node]
    if node=='end':
            return [visited]
    path = []
    for cave in caves[node]:
        if cave in visited and caveSize(cave) == 'small':
            pass
        else:
            paths = navigateTo(cave,visited)
            for a_path in paths:
                path.append(a_path)
    return path
        
   
if __name__ == "__main__":
    data = readPuzzleInput()
    print("The answer to part 1;")
    part1(data)
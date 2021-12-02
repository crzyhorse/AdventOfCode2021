def readpuzzleinput():
    data = []
    with open ('day2puzzleinput.txt', 'r') as datafile:
        data = [tuple(int(x) if x.isdigit() else x for x in x.strip().split()) for x in datafile.readlines()]
    return data

def output(horizontal,depth):
    print("Horizontal position is {}".format(horizontal))
    print("Depth is {}".format(depth))
    print("Multiplied is {}".format(horizontal*depth))
    
def part2(directions):
    aim = 0
    horizontal = 0
    depth = 0
    for direction, amount in directions:
        if direction == "forward":
            horizontal += amount
            if aim > 0:
                depth += amount * aim
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
        else:
            raise "Unknown direction given"
    output(horizontal, depth)

def part1(directions):
    horizontal = 0
    depth = 0
    for direction, amount in directions:
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
        else:
            raise "Unknown direction given"
    output(horizontal, depth)

if __name__ == "__main__":
    directions = readpuzzleinput()
    print("The answers to part 1 are;")
    part1(directions)
    print("The answers to part 2 are;")
    part2(directions)
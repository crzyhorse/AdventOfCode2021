"""
Part 1
    Your horizontal position and depth both start at 0. 

        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2

    forward 5 adds 5 to your horizontal position, a total of 5.
    down 5 adds 5 to your depth, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13.
    up 3 decreases your depth by 3, resulting in a value of 2.
    down 8 adds 8 to your depth, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15.
    After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Part 2 
    In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.
    Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

    Now, the above example does something different:

    forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
    down 5 adds 5 to your aim, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
    up 3 decreases your aim by 3, resulting in a value of 2.
    down 8 adds 8 to your aim, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
    After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

"""
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
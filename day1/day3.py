"""
Part 1
    Power = Decimal(Gamma Rate * Epsilon Rate)
    Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
    The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
    The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

    So, the gamma rate is the binary number 10110, or 22 in decimal.

    The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. 
    So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Part 2    
    Start with the full list of binary numbers and consider just the first bit of those numbers. Then:

    Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
    If you only have one number left, stop; this is the rating value for which you are searching.
    Otherwise, repeat the process, considering the next bit to the right.
    The bit criteria depends on which type of rating value you want to find:

    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
    For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

    Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
    Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
    In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
    In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
    In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
    As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
    Then, to determine the CO2 scrubber rating value from the same example above:

    Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
    Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
    In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
    As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
    Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

    Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

"""
from bitstring import BitArray

def readpuzzleinput():
    data = []
    with open ('day3puzzleinput.txt', 'r') as datafile:
        data = [x.strip() for x in datafile.readlines()]
    return data
    

def countBits(data):
    numDigits = range(len(data[0]))
    counters = [0 for digits in numDigits]
    for string in data:
        for i in numDigits:
            if string[i] == "1":
                counters[i] +=1
    return counters

def part1(data):
    numEntries = len(data)
    numDigits = range(len(data[0]))
    # i used a BitArray in part 1 because it let me be lazy since 
    # a) i can easily set each individual bit, compared to converting a string of bits to a list and back
    # b) you can easily invert a bit array, not so much a string of bits.
    bits = BitArray(length=12) 
    bits.set(0)
    counters = countBits(data)
    for i in numDigits:
        numOnes = counters[i]
        numZeros = numEntries - numOnes
        if numOnes > numZeros:
            bits.set(1,i)
        else:
            bits.set(0,i)
    epsilon = bits.uint
    bits.invert()
    gamma = bits.uint
    print("Epsilon is {}".format(epsilon))
    print("Gamma is {}".format(gamma))
    print("Power Consumption is {}".format(epsilon*gamma))

    
def part2(data):
    numDigits = range(len(data[0]))
    foundValues = {}
    originalData = data
    originalCounters = countBits(data)
    for valueType in ["oxygen generator", "co2 scrubber"]:
        data = originalData
        numEntries = len(data)
        counters = originalCounters

        for i in numDigits:
            numOnes = counters[i]
            numZeros = numEntries - numOnes
            if numOnes > numZeros:
                mostCommon = "ones"
            elif numOnes < numZeros:
                mostCommon = "zeros"
            elif numOnes == numZeros:
                mostCommon = "equal"

            if valueType == "oxygen generator":
                if mostCommon == "ones":
                    data = [x for x in data if x[i] == "1"]
                elif mostCommon == "zeros":
                    data = [x for x in data if x[i] == "0"]
                elif mostCommon == "equal":
                    data = [x for x in data if x[i] == "1"]
            elif valueType == "co2 scrubber":
                if mostCommon == "ones":
                    data = [x for x in data if x[i] == "0"]
                elif mostCommon == "zeros":
                    data = [x for x in data if x[i] == "1"]
                elif mostCommon == "equal":
                    data = [x for x in data if x[i] == "0"]

            if len(data) == 1:
                foundValues[valueType] = int(data[0],2)
                break
            if len(data) == 0:
                raise "Should never get an empty list"
            
            numEntries = len(data)
            counters = countBits(data)

        print("Value for {} is {}".format(valueType,foundValues[valueType]))
    print("Life Support rating is {}".format(foundValues["oxygen generator"]*foundValues["co2 scrubber"]))

if __name__ == "__main__":
    data = readpuzzleinput()
    print("The answers for part 1 are;")
    part1(data)
    print("The answers for part 2 are;")
    part2(data)
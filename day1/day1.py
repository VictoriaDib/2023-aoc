import re

def day1_part2(input):
    sum = 0

    digits = {
        "one" : "o1e",
        "two" : "t2o",
        "three" : "t3e",
        "four" : "f4r",
        "five" : "f5e",
        "six" : "s6x",
        "seven" : "s7n",
        "eight" : "e8t",
        "nine" : "n9e"
    }
    
    with open (input, 'r') as f:
        read = f.readlines()
        for line in read:
            # print("Line: ", line)

            indices = []
            for d in digits:
                match = re.search(d,line)
                if match:
                    indices.append((match.group() ))

            for i in indices:
                line = re.sub(i, digits[i], line)

            nums = []
            for c in line:
                if c.isdigit():
                    nums.append(c)
                    
            if nums:
                n = nums[0] + nums[-1]
                sum += int(n)

    return sum


def day1_part1(input):
    sum = 0

    with open (input, 'r') as f:
        for line in f:
            nums = [] 
            for c in line:
                if c.isdigit():
                    nums.append(c)
            if nums:
                n = nums[0] + nums[-1]
                sum += int(n)

    return sum


# smaller inputs
d1p1 = day1_part1("pt1small.txt")
assert d1p1 == 142, f"got: {d1p1}"

d1p2 = day1_part2('pt2small.txt')
assert d1p2 == 281, f"got: {d1p2}"

# full input
print("part 2: ", day1_part1('day1-input.txt'))
print("part 2: ", day1_part2('day1-input.txt'))
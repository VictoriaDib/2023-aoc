import re

def score(x):
    return 1 << (x-1)


with open("small.txt","r") as f:
    copies = dict()
    sum = 0
    for line in f.readlines():
        line = line.strip()
        # print(line)
        id = int(line[5:line.index(':')])
        if id not in copies:
            copies[id] = 1
        else:
            copies[id] +=1
        print(id)
        line = line[line.index(': ')+2:]
        line = line.split(" | ")
        winning = set([int(x) for x in line[0].split()])
        have    = set([int(x) for x in line[1].split()])
        common = len(winning.intersection(have))
        if common:
            # print(common, "matches is worth ", 1<<max(0,common-1), "points.")
            sum += score(common)

        for i in range(id+1, (id+common)+1):
            print(copies)
            if i in copies:
                print("copiy:",copies[i])
                copies[i] += 1
            else:
                copies[i] = 1
            print("Card",id ," won copies of cards:",i)

        for k,v in copies.items():
            for i in range(v,1,-1):
                print("stepping:", i)
    print("Part 2:", copies)

    # print(">>", 8>>)

    print("Part 1:",sum)
        

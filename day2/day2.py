RED = 12
GREEN = 13
BLUE = 14

sum = 0
power = 0

with open("input.txt", 'r') as f:
    read = f.readlines()
    for line in read:
        line = line.replace(":",";")
        sets = line.split("; ")

        id = sets[0].split(" ")[1]

        ok = True

        reds = []
        greens = []
        blues = []

        for item in sets[1:]:
            spl = item.split(", ")
            for e in spl:
                e = e.split(" ")
                count = int(e[0])
                color = e[1]
                
                if "red" in color:
                    reds.append(count)
                    if count > RED:
                        ok = False
                if "green" in color:
                    greens.append(count)
                    if count > GREEN:
                        ok = False
                if "blue" in color:
                    blues.append(count)
                    if count > BLUE:
                        ok = False
                        
        r = max(reds)
        g = max(greens)
        b = max(blues)

        power += r*g*b

        if not ok:
            continue
        else:
            sum += int(id)
        

print("part 1: ", sum)
print("part 2: ", power)

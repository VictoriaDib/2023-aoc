import sys

data = open(sys.argv[1]).read().strip()

time,dis = data.split("\n")



t = [int(x) for x in time.split(":")[1].split()]
d = [int(x) for x in dis.split(":")[1].split()]

t2 = int("".join(str(n) for n in t))
d2 = int("".join(str(n) for n in d))

def calc(t, d):
    total = 1

    for k in range(len(t)):
        count = 0

        for i in range(0, t[k]+1):
            s = i * (t[k] - i)
            # print("held button for", i, "ms and distance traveled: ", s, " mm by the end of the race.")
            if s != 0 and s > d[k]:
                count +=1
        # print("Possible ways:", count)

        total *= count
    return total

print("P1 total ways:", calc(t,d))
print("P2 total ways:", calc([t2],[d2]))




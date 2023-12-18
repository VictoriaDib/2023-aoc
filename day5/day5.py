import re


def in_range(seed, src, r):
    return seed in range(src, src+r)

def set_seed(m, seed, dest, src, r):
    src = s2s[1]
    dest = s2s[0]

    if in_range(seed,src,r):
        m[seed] = dest+(seed-src)
    elif seed not in m:
        m[seed] = seed

def get_num(m, n, seed, dest, src, r):
    src = s2s[1]
    dest = s2s[0]

    if in_range(seed,src,r):
        temp = m[seed]
        n[temp] = dest+(seed-src)
    elif seed not in n:
        n[m[seed]] = m[seed]



with open("small.txt", "r") as f:
    read = f.read().strip()
    # L = read.split('\n')
    
    maps = read.split('\n\n')

    # print("L: ", L)
    print("Maps: ", maps)

    seeds = [int(i) for i in maps[0].split(":")[1].split()]
    # print(seeds)
    maps = read.split('\n\n')

    seeds2soil = [x.split() for x in maps[1].split(":\n")[1].split("\n")]
    seeds2soil=[list(map(int,group)) for group in seeds2soil]
    print(seeds2soil)

####
    seedsoil = {}
    for seed in seeds: 
        for s2s in seeds2soil:
            src = s2s[1]
            dest = s2s[0]
            r = s2s[2]

            set_seed(seedsoil, seed, dest,src,r)
    
    print(seedsoil)


##### soil2fert
    soil2fert = [x.split() for x in maps[2].split(":\n")[1].split("\n")]
    soil2fert =[list(map(int,group)) for group in soil2fert]
    print("soil2fert",soil2fert)

    p1 = {}
    for k in seedsoil:
        for s2s in soil2fert:
            src = s2s[1]
            dest = s2s[0]
            r = s2s[2]
            
            get_num(seedsoil,p1, k, dest,src,r)
        
    # seedsoil = p1
    # print(seedsoil)
    print(p1)    

### fert2water 
    fert2water = [x.split() for x in maps[3].split(":\n")[1].split("\n")]

    # does python have maps



    # fert2water = [x.split() for x in maps[3].split(":\n")[1].split("\n")]
    # water2light = [x.split() for x in maps[4].split(":\n")[1].split("\n")]
    # light2temp = [x.split() for x in maps[5].split(":\n")[1].split("\n")]
    # temp2humid = [x.split() for x in maps[6].split(":\n")[1].split("\n")]
    # humid2loc = [x.split() for x in maps[7].split(":\n")[1].split("\n")]


    # print(seeds)
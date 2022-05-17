# Heuristic values
dict_hn={'A':336,'B':0,'C':160,'D':242,}

# real values
dict_gn=dict(
    A=dict(B=190,D=120,C=211),
    B=dict(A=190,C=138,D=120),
    C=dict(B=138,A=211),
    D=dict(B=120,A=120),
)

import queue as Q
#from RMP import dict_gn #from RMP import dict_hn
start='A'
goal='C'
result=''

def get_fn(citystr):
    cities=citystr.split(" , ")
    hn = gn= 0
    for ctr in range(0, len(cities)-1):
        gn = gn+dict_gn[cities[ctr]][cities[ctr+1]]
        hn = dict_hn[cities[len(cities)-1]]
    return(hn+gn)

def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get()
    if thiscity == goal:
        result=citystr+" : : "+str(tot)
        return

    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
    expand(cityq)

def main():
    cityq = Q.PriorityQueue()
    thiscity = start
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)

main()

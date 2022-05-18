# Heuristic values
dict_hn={'A':11,'B':6,'C':99,'D':1,'E':7,'G':0}

# real values
dict_gn=dict(
    A=dict(B=2,E=3),
    B=dict(C=1,G=9),
    C=0,
    D=dict(G=1),
    E=dict(D=6)
)

import queue as Q

start='A'
goal='G'
result=''

def get_fn(Nodestr):
    Nodes=Nodestr.split(" , ")
    hn = gn = 0
    for i in range(0, len(Nodes)-1):
        gn = gn+dict_gn[Nodes[i]][Nodes[i+1]]
        hn = dict_hn[Nodes[len(Nodes)-1]]
    return(hn+gn)

def expand(Nodeq):
    global result
    tot, Nodestr, thisNode = Nodeq.get()
    if thisNode == goal:
        result=Nodestr+" : : "+str(tot)
        return

    for nod in dict_gn[thisNode]:
        Nodeq.put((get_fn(Nodestr+" , "+nod), Nodestr+" , "+nod, nod))
    expand(Nodeq)

def main():
    Nodeq = Q.PriorityQueue()
    thisNode = start
    Nodeq.put((get_fn(start),start,thisNode))
    expand(Nodeq)
    print("The A* path with the total is: ")
    print(result)

main()

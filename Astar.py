# Heuristic values
dict_hn={'A':336,'B':0,'C':160,'D':242}

# real values
dict_gn=dict(
    A=dict(B=190,D=120,C=211),
    B=dict(A=190,C=138,D=120),
    C=dict(B=138,A=211),
    D=dict(B=120,A=120),
)

import queue as Q

start='A'
goal='C'
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

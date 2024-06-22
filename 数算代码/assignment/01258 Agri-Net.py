import heapq
def prim(start):
    path=[]
    used=set([start])
    edge=[(cost,start,to) for to,cost in gra[start].items()]
    heapq.heapify(edge)
    while edge:
        cost,frm,to=heapq.heappop(edge)
        if to not in used:
            used.add(to)
            path.append((frm,to,cost))
            for to2,cost2 in gra[to].items():
                if to2 not in used:
                    heapq.heappush(edge,(cost2,to,to2))
    return sum(x[2] for x in path)

while True:
    try:
        n=int(input())
        gra={i:{} for i in range(n)}
        for i in range(n):
            l=list(map(int,input().split()))
            for k in range(n):
                if l[k]!=0:
                    gra[i][k]=l[k]
                    gra[k][i]=l[k]
        ans=100001*n
        ans=min(prim(i),ans)
        print(ans)
    except EOFError:
        break
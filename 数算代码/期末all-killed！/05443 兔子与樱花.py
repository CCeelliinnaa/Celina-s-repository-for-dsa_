from heapq import heappop,heappush
from collections import defaultdict
def dijkstra(start,end):
    heap=[(0,start,[start])]
    vis=set()
    while heap:
        (cost,u,path)=heappop(heap)
        if u not in vis:
            vis.add(u)
            if u==end:
                return [cost,path]
            for v in graph[u]:
                if v not in vis:
                    heappush(heap,(cost+graph[u][v],v,path+[v]))

n=int(input())
name=[]
for i in range(n):
    name.append(input())
graph=defaultdict(dict)
for i in range(int(input())):
    x,y,l=input().split()
    graph[x][y]=graph[y][x]=int(l)

N=int(input())
for i in range(N):
    start,end=input().split()
    cost,path=dijkstra(start,end)
    for j in range(len(path)-1):
        print(f'{path[j]}->({graph[path[j]][path[j+1]]})->',end='')
    print(path[-1])
def isCyclicKahn(graph,V):
    in_degree=[0]*V
    for u in range(V):
        for v in graph[u]:
            in_degree[v]+=1

    queue=[]
    for i in range(V):
        if in_degree[i]==0:
            queue.append(i)

    count=0
    while queue:
        u=queue.pop(0)
        count+=1
        for v in graph[u]:
            in_degree[v]-=1
            if in_degree[v]==0:
                queue.append(v)
    return count!=V


T=int(input())
ans=[]
for _ in range(T):
    N, M=map(int,input().split())
    graph=[[] for _ in range(N)]
    for _ in range(M):
        u,v=map(int,input().split())
        graph[u-1].append(v-1)
    ans.append("Yes" if isCyclicKahn(graph,N) else "No")

for i in ans:
    print(i)
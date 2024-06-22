import heapq

K,N,R=[int(input()) for i in range(3)]
road={i:[] for i in range(1,N+1)}
for i in range(R):
    s,e,l,cost=map(int,input().split())
    road[s].append((e,l,cost))
q=[(0,1,0)]
visited=[0 for i in range(N+1)]
while q:
    [l,s,cost]=heapq.heappop(q)
    if s==N:
        print(l)
        exit()
    if visited[s]==0 or visited[s]>cost:
        visited[s]=cost
        for i in road[s]:
            if i[2]+cost<=K:
                heapq.heappush(q,(i[1]+l,i[0],i[2]+cost))
print(-1)
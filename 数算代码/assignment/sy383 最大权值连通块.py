a=0
def dfs(vertex):
    global a
    if visited[vertex]==True:
        return
    visited[vertex]=True
    a+=v_value[vertex]
    for i in edge[vertex]:
        dfs(i)

n,m=map(int,input().split())
v_value=list(map(int,input().split()))
edge={}
for i in range(n):
    edge[i]=[]
for i in range(m):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)


ans=0
for i in range(n):
    visited=[False]*n
    a=0
    dfs(i)
    ans=max(ans,a)

print(ans)
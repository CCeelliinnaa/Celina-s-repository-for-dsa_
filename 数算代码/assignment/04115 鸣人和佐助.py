dire=[(-1,0),(0,-1),(1,0),(0,1)]
ans=0
flag=0
def bfs(x,y,t):
    global ans,flag
    q=[]
    visited=set()
    q.append((t,x,y,0))
    while q:
        t,x,y,ans=q.pop(0)
        for dx,dy in dire:
            nx=x+dx
            ny=y+dy
            if 0<=nx<m and 0<=ny<n:
                if gra[nx][ny]!="#":
                    nt=t
                else:
                    nt=t-1
                if nt>=0 and (nt,nx,ny) not in visited:
                    nans=ans+1
                    if gra[nx][ny]=="+":
                        flag=1
                        return flag,nans
                    q.append((nt, nx, ny, nans))
                    visited.add((nt,nx,ny)) ###！！！！
    return flag,ans

m,n,t=map(int,input().split())
gra=[]
for i in range(m):
    s=input()
    gra.append(s)
for i in range(m):
    for j in range(n):
        if gra[i][j]=='@':
            x=i
            y=j
flag,ans=bfs(x,y,t)
if flag:
    print(ans)
else:
    print(-1)
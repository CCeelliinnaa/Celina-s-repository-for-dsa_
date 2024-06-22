move=[(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]
cnt=0
def dfs(x,y):
    global cnt
    cnt+=1
    visited[x][y]=1
    for dx,dy in move:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<m and gra[nx][ny]=='W' and visited[nx][ny]==0:
            dfs(nx,ny)
    return cnt

T=int(input())
out=[]
for _ in range(T):
    n,m=map(int,input().split())
    gra=[]
    ans=0
    visited=[[0]*m for i in range(n)]
    for i in range(n):
        gra.append(list(input()))
    for i in range(n):
        for j in range(m):
            if gra[i][j]=='W' and visited[i][j]==0:
                cnt=0
                dfs(i,j)
                ans=max(ans,cnt)
    out.append(ans)
for i in out:
    print(i)
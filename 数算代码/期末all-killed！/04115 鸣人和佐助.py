m,n,t=map(int,input().split())
move=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(sx,sy,ex,ey):
    min_t=float('inf')
    q=[(sx,sy,0,t)]
    visited=set()
    flag=False
    while q:
        x,y,time,left_t=q.pop(0)
        if x==ex and y==ey:
            min_t=min(min_t,time)
            flag=True
        for dx,dy in move:
            nx=x+dx
            ny=y+dy
            if 0<=nx<m and 0<=ny<n:
                if gra[nx][ny]=='#' and left_t>0 and (nx,ny,left_t) not in visited:
                    nt=left_t-1
                    q.append((nx,ny,time+1,nt))
                    visited.add((nx,ny,nt))
                elif gra[nx][ny]!='#' and (nx,ny,left_t) not in visited:
                    nt=left_t
                    q.append((nx,ny,time+1,left_t))
                    visited.add((nx,ny,nt))
    return flag,min_t

gra=[]
for i in range(m):
    l=list(input())
    for k in range(len(l)):
        if l[k]=='@':
            sx,sy=i,k
        if l[k]=='+':
            ex,ey=i,k
    gra.append(l)
stat,ans=bfs(sx,sy,ex,ey)
if stat:
    print(ans)
else:
    print(-1)
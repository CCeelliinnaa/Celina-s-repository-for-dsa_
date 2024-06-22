move=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
ans=0
def dfs(n,m,x,y,cnt):
    ma[x][y]=1
    global ans
    if cnt==n*m:
        ans+=1
        return
    for i in range(8):
        if 0<=x+move[i][0]<n and 0<=y+move[i][1]<m and ma[x+move[i][0]][y+move[i][1]]==0:
            dfs(n,m,x+move[i][0],y+move[i][1],cnt+1)
            ma[x+move[i][0]][y+move[i][1]]=0 ##!!!!

N=int(input())
a=[]
for i in range(N):
    n,m,x,y=map(int,input().split())
    ma=[[0]*(m) for i in range(n)]
    ans=0
    dfs(n,m,x,y,1)
    a.append(ans)
    
for i in a:
    print(i)
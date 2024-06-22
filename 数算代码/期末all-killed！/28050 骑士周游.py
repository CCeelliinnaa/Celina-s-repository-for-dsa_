move=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
ans=0
def getNeighbor(x,y):
    return [(x+dx,y+dy) for dx,dy in move if 0<=x+dx<n and 0<=y+dy<n and visited[x+dx][y+dy]==0]

def dfs(x,y,cnt):
    visited[x][y]=1
    global ans
    if cnt==n*n:
        return True
    for x2,y2 in sorted(getNeighbor(x,y),key=lambda c:len(getNeighbor(c[0],c[1]))):
        if dfs(x2,y2,cnt+1):
            return True ##!!!!!!!!!
        visited[x2][y2]=0

n=int(input())
x,y=map(int,input().split())
visited=[[0]*n for i in range(n)]
ans=0
print('success' if dfs(x,y,1) else 'fail')
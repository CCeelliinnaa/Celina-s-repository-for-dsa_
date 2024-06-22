move=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
ans=0
def getNeighbor(x,y):
    return [(x+dx,y+dy) for dx,dy in move if 0<=x+dx<n and 0<=y+dy<n and graph[x+dx][y+dy]]

def dfs(x,y,cnt):
    graph[x][y]=0
    global ans
    if cnt==n*n:
        return True
    for x2,y2 in sorted(getNeighbor(x,y),key=lambda c:len(getNeighbor(c[0],c[1]))):
        if graph[x2][y2]:
            if dfs(x2,y2,cnt+1):
                return True
            graph[x2][y2]=1

n=int(input())
x,y=map(int,input().split())
graph=[[1]*n for i in range(n)]
ans=0
print('success' if dfs(x, y, 1) else 'fail')
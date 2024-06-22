dire=[(0,-1),(0,1),(-1,0),(1,0)]
def dfs(i,j):
    vis[i][j]=1
    for dx,dy in dire:
        if 0<=i+dx<10 and 0<=j+dy<10 and vis[i+dx][j+dy]==0 and gra[i][j]=='.':
            dfs(i+dx,j+dy)
    return

gra=[]
cnt=0
vis=[[0]*10 for i in range(10)]
for i in range(10):
    s=input()
    gra.append(s)
for i in range(10):
    for j in range(10):
        if gra[i][j]=='.' and vis[i][j]==0:
            dfs(i,j)
            cnt+=1
print(cnt)
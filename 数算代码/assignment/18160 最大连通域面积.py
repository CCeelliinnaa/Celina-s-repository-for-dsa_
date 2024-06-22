a=0
move=[[0,1],[0,-1],[1,1],[1,-1],[1,0],[-1,1],[-1,-1],[-1,0]]
def dfs(i,j):
    global a
    if mat[i][j]=='.':
        return
    mat[i][j]='.'
    a+=1
    for k in range(8):
        dfs(i+move[k][0],j+move[k][1])
    


N=int(input())
output=[]
for k in range(N):
    mat=[]
    ans=0
    n,m=map(int,input().split())
    mat.append(['.']*(m+2))
    for i in range(n):
        s=['.']+list(input())+['.']
        mat.append(s)
    mat.append(['.']*(m+2))
    for i in range(1,n+1):
        for j in range(1,m+1):
            if mat[i][j]=='W':
                a=0
                dfs(i,j)
                ans=max(ans,a)
    output.append(ans)

for i in output:
    print(i)
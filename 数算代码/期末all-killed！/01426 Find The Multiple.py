def bfs(x):
    q=[(1,'1')]
    while q:
        mol,cur=q.pop(0)
        for i in ['0','1']:
            if mol==0:
                return cur
            if visited[(mol*10+int(i))%x]==0:
                q.append(((mol*10+int(i))%x,cur+i))
                visited[(mol*10+int(i))%x]=1

ans=[]
while True:
    x=int(input())
    visited=[0]*x
    if x==0:
        break
    ans.append(bfs(x))
for i in ans:
    print(i)
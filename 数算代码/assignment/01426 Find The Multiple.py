def bfsmol(n):
    q=[]
    q.append((1%n,"1"))
    visited=set([1%n])
    while q:
        mol,num=q.pop(0)
        if mol==0:
            return num
        for i in ['0','1']:
            if (mol*10+int(i))%n not in visited:
                q.append(((mol*10+int(i))%n,num+i))
                visited.add((mol*10+int(i))%n)

ans=[]
while True:
    n=int(input())
    if n==0:
        break
    ans.append(bfsmol(n))
for i in ans:
    print(i)
def bfs():
    q=[1]
    l=[1]
    while q:
        for i in range(len(q)):
            x=q.pop(0)
            for k in tree[x]:
                if k!=-1: 
                    q.append(k)
        if q:
            l.append(q[-1])
    return l


n=int(input())
tree={i:[] for i in range(1,n+1)}
for i in range(1,n+1):
    l,r=map(int,input().split())
    tree[i].append(l)
    tree[i].append(r)
l=bfs()
print(' '.join(map(str,l)))
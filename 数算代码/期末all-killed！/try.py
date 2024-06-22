class UnionFind:
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[1]*size

    def find(self,p):
        if self.parent[p]!=p:
            self.parent[p]=self.find(self.parent[p])
        return self.parent[p]

    def union(self,p,q):
        rootP=self.find(p)
        rootQ=self.find(q)
        if rootP!=rootQ:
            if self.rank[rootP]>self.rank[rootQ]:
                self.parent[rootQ]=rootP
            elif self.rank[rootP]<self.rank[rootQ]:
                self.parent[rootP]=rootQ
            else:
                self.parent[rootQ]=rootP
                self.rank[rootP]+=1

N=int(input())
ans=[]
for _ in range(N):
    n,x=map(int,input().split())
    unset=UnionFind(n+1)
    has_cycle=False
    for i in range(x):
        a,b=map(int,input().split())
        if unset.find(a)==unset.find(b):
            has_cycle=True
            break
        else:
            unset.union(a,b)
    ans.append('No' if has_cycle else 'Yes')
for i in ans:
    print(i)
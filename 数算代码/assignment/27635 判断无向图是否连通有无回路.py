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

v,e=map(int,input().split())
unset=UnionFind(v)
has_cycle=False
is_connected=True
edges=[]
for i in range(e):
    a,b=map(int,input().split())
    edges.append((a,b))

for a,b in edges:
    if unset.find(a)==unset.find(b):
        has_cycle=True
    else:
        unset.union(a,b)

root=unset.find(0)
for i in range(1,v):
    if unset.find(i)!=root:
        is_connected=False
        break

print("connected:yes" if is_connected else "connected:no")
print("loop:no" if has_cycle==False else "loop:yes")
class DisjointSet():
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

n,m=map(int,input().split())
unset=DisjointSet(n)
for i in range(m):
    a,b=map(int,input().split())
    if unset.find(a)!=unset.find(b):
        unset.union(a,b)
find=set()
cnt=0
for i in range(1,n+1):
    if unset.find(i) not in find:
        find.add(unset.find(i))
        cnt+=1
print(cnt)
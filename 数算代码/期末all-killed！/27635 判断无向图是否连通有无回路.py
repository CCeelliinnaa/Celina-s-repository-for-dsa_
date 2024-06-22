class DisjointSet():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n)

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
has_cycle=False
is_connected=True
for i in range(m):
    a,b=map(int,input().split())
    if unset.find(a)==unset.find(b):
        has_cycle=True
    else:
        unset.union(a,b)
root=unset.find(0)
for i in range(n):
    if unset.find(i)!=root:
        is_connected=False
        break
print(f"connected:{'yes' if is_connected else 'no'}")
print(f"loop:{'yes' if has_cycle else 'no'}")
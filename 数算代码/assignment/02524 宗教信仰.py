class DisjointSet:
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

def estimate_religions(n,edges):
    dsu = DisjointSet(n)
    for i, j in edges:
        dsu.union(i, j)
    religions = set()
    for i in range(1, n+1):
        religions.add(dsu.find(i))

    return len(religions)

cnt=0
while True:
    cnt+=1
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    edges = []
    for _ in range(m):
        i, j = map(int, input().split())
        edges.append((i, j))
    max_religions = estimate_religions(n,edges)
    print(f"Case {cnt}: {max_religions}")
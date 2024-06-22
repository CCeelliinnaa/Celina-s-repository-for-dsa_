class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
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

def kruskal(n,edges):
    uf=UnionFind(n)
    edges.sort(key=lambda x:x[2])
    mst,max_edge=0,0
    for u, v, w in edges:
        if uf.find(u)!=uf.find(v):
            uf.union(u, v)
            mst+=1
            max_edge=max(max_edge,w)
            if mst==n-1:
                break
    return mst, max_edge

v,e=map(int,input().split())
edges=[]
for i in range(e):
    a,b,value=map(int,input().split())
    edges.append((a,b,value))
mst,max_edge=kruskal(e,edges)
print(f'{mst} {max_edge}')
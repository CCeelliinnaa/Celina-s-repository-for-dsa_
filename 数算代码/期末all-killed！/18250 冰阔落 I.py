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
        self.parent[root_v] = root_u

while True:
    try:
        n,m=map(int,input().split())
        ans=[]
        unset=DisjointSet(n)
        for i in range(m):
            a,b=map(int,input().split())
            if unset.find(a)==unset.find(b):
                ans.append('Yes')
            else:
                unset.union(a,b)
                ans.append('No')
        root=set()
        for i in range(1,n+1):
            root.add(unset.find(i))
        ans.append(len(root))
        root=list(root)
        ans.append(' '.join(map(str,sorted(root))))
        for i in ans:
            print(i)

    except EOFError:
        break

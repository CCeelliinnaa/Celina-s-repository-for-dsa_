class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # 路径压缩
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # 按秩合并
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

def is_connected_and_has_cycle(edges, num_nodes):
    uf = UnionFind(num_nodes)
    has_cycle = False
    
    for u, v in edges:
        if uf.find(u) == uf.find(v):
            has_cycle = True  # 如果两个端点已经在同一个集合中，则有回路
        else:
            uf.union(u, v)
    
    # 检查连通性
    root = uf.find(0)
    for i in range(1, num_nodes):
        if uf.find(i) != root:
            return False, has_cycle  # 图不连通

    return True, has_cycle  # 图连通

# 示例
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
num_nodes = 5

is_connected, has_cycle = is_connected_and_has_cycle(edges, num_nodes)
print(f"图是否连通: {is_connected}")
print(f"图是否有回路: {has_cycle}")

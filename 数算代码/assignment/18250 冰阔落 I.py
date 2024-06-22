class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

while True:
    try:
        n, m = map(int, input().split())
        disjoint_set = DisjointSet(n)
        ice_cold = set(range(1, n + 1))

        for _ in range(m):
            x, y = map(int, input().split())
            if disjoint_set.find(x) == disjoint_set.find(y):
                print("Yes")
            else:
                print("No")
                disjoint_set.union(x, y)

        ice_cold_count = 0
        ice_cold_cups = []
        for cup in ice_cold:
            if disjoint_set.find(cup) == cup:
                ice_cold_count += 1
                ice_cold_cups.append(cup)

        print(ice_cold_count)
        ice_cold_cups.sort()
        for result in ice_cold_cups:
            print(result,end=' ')
    except EOFError:
        break
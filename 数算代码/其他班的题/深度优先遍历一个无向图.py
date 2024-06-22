def dfs(graph, visited, node):
    visited[node] = True
    print(node, end=" ")

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i)

if __name__ == "__main__":
    main()
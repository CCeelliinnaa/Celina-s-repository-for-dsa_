import heapq
def dijkstra(graph, start):
    m, n = len(graph), len(graph[0])
    distances = {(i,j): float('inf') for i in range(m) for j in range(n)}
    distances[(start[0],start[1])] = 0
    priority_queue = [(0,start)]
    while priority_queue:
        current_distance,(cx, cy)=heapq.heappop(priority_queue)
        if current_distance>distances[(cx, cy)]:
            continue
        for dx,dy in [(0,-1),(0,1),(1,0),(-1,0)]:
            nx,ny=cx+dx,cy+dy
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]!='#':
                new_distance=current_distance+abs(int(graph[nx][ny])-int(graph[cx][cy]))
                if new_distance<distances[(nx, ny)]:
                    distances[(nx,ny)]=new_distance
                    heapq.heappush(priority_queue,(new_distance,(nx,ny)))
    return distances

m,n,p=map(int,input().split())
graph=[]
for _ in range(m):
    row=input().split()
    graph.append(row)
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if graph[x1][y1]== '#' or graph[x2][y2]=='#':
        print('NO')
        continue
    distances=dijkstra(graph, (x1, y1))
    if (x2, y2) in distances and distances[(x2, y2)]!=float('inf'):
        print(distances[(x2, y2)])
    else:
        print('NO')
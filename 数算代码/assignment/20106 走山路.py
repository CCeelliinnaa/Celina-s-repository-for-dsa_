dire=[(0,-1),(0,1),(1,0),(-1,0)]
def bfs(x,y):
    q=[(x,y)]
    distances={(x,y):0}
    while q:
        cx,cy=q.pop(0)
        for dx,dy in dire:
            nx,ny=cx+dx,cy+dy
            if 0<=nx<m and 0<=ny<n and gra[nx][ny] != '#':
                new_distance=distances[(cx, cy)]+abs(int(gra[nx][ny])-int(gra[cx][cy]))
                if (nx,ny) not in distances or new_distance<distances[(nx,ny)]:
                    distances[(nx,ny)]=new_distance
                    q.append((nx,ny))
    return distances

m,n,p=map(int,input().split())
gra=[]
for _ in range(m):
    s=input().split()
    gra.append(s)
for _ in range(p):
    x1,y1,x2,y2 = map(int, input().split())
    if gra[x1][y1]=='#' or gra[x2][y2]=='#':
        print('NO')
        continue
    distances=bfs(x1, y1)
    if (x2,y2) in distances:
        print(distances[(x2,y2)])
    else:
        print('NO')
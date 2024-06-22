def bfs(a,b,c):
    q=[(0,0,[])]
    vis=set()
    vis.add((0, 0))
    while q:
        cur_a,cur_b,steps=q.pop(0)
        if cur_a==c or cur_b==c:
            return steps
        new=[
            (a,cur_b,steps+['FILL(1)']),(cur_a,b,steps+['FILL(2)']),
            (0,cur_b,steps+['DROP(1)']),(cur_a,0,steps+['DROP(2)']),
            (max(0,cur_a-(b-cur_b)),min(b,cur_b+cur_a),steps+['POUR(1,2)']),
            (min(a,cur_a+cur_b),max(0,cur_b-(a-cur_a)),steps+['POUR(2,1)']),
            ]
        for new_a,new_b,new_steps in new:
            if (new_a,new_b) not in vis:
                vis.add((new_a,new_b))
                q.append((new_a,new_b,new_steps))
    return "impossible"

a,b,c=map(int,input().split())
ans=bfs(a,b,c)
if ans=="impossible":
    print(ans)
else:
    print(len(ans))
    for step in ans:
        print(step)
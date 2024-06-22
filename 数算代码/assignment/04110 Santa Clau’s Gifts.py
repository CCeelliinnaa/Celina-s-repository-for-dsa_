n,w=map(int,input().split())
ruo=[]
for i in range(n):
    a,b=map(int,input().split())
    ruo.append([a,b])
ruo.sort(key=lambda x:x[0]/x[1],reverse=True)
ans=0
for i in range(len(ruo)):
    if w>=ruo[i][1]:
        w-=ruo[i][1]
        ans+=ruo[i][0]
    else:
        ans+=ruo[i][0]/ruo[i][1]*w
        break
print(f'{ans:.1f}')
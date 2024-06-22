n=int(input())
l=list(map(int,input().split()))
ans=[0]*n
s=[]
for i in range(n-1,-1,-1):
    while s:
        x=s[-1]
        if l[x]>l[i]:
            ans[i]=x+1
            break
        else:
            s.pop()
    s.append(i)
print(*ans)
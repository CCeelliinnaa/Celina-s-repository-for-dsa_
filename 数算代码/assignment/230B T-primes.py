def prime():
    for i in range(2,1000001):
        if p[i]==1:
            for i in range(2*i,1000001,i):
                p[i]=0
p=[1]*1000001
prime()
p[0]=p[1]=0

import math
ans=[]
n=int(input())
num=list(map(int,input().split()))
for t in num:
    if int(math.sqrt(t))**2==t and p[int(math.sqrt(t))]==1:
        ans.append('YES')
    else:
        ans.append('NO')
for i in ans:
    print(i)
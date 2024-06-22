def prime():
    for i in range(2,10001):
        if p[i]==1:
            for i in range(2*i,10001,i):
                p[i]=0
p=[1]*10001
prime()
p[0]=p[1]=0
import math
ans=[]
n,m=map(int,input().split())
for i in range(n):
    l=list(map(int,input().split()))
    sum=0
    total=len(l)
    for i in range(len(l)):
        if int(math.sqrt(l[i]))**2==l[i] and p[int(math.sqrt(l[i]))]==1:
            sum+=l[i]
    if sum==0:
        ans.append(0)
    else:
        ans.append(f'{sum/total:.2f}')
for i in ans:
    print(i)
import math
n=int(input())
ans=[]
for i in range(n):
    a=int(input())
    sum=(1+a)*a//2
    t=int(math.log2(a))
    sum-=(2**(t+1)-1)*2
    ans.append(sum)
for i in ans:
    print(i)
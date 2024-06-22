n,m=map(int,input().split())
def check(x):
    sum=0
    cnt=1  ####是从1开始的！！！！！
    for i in range(n):
        if sum+cost[i]>x:
            sum=cost[i]
            cnt+=1
        else:
            sum+=cost[i]
    if cnt>m:
        return False
    else:
        return True


cost=[]
for i in range(n):
    cost.append(int(input()))
maxmax=sum(cost)
minmax=max(cost)
l=minmax
r=maxmax
while l<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid+1
print(l)
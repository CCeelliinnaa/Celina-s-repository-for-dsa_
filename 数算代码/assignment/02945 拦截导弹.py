n=int(input())
height=list(map(int,input().split()))
dp=[1]*len(height)
ans=0
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if height[i]>=height[j]:
            dp[i]=max(dp[i],dp[j]+1)
    ans=max(ans,dp[i])
print(ans)
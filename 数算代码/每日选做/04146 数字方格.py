n=int(input())
ans=0
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if (i+j)%2==0 and (j+k)%3==0 and (i+j+k)%5==0:
                ans=max(ans,i+j+k)
print(ans)
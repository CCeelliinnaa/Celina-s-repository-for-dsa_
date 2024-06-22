s=list(input())
n=len(s)
t=1
temp=[]
while t<=n:
    temp.append(s[t-1])
    t*=2
ans1=[]
m=len(temp)
for i in range(m):
    ans1.append(temp[i])
    ans1.append(temp[m-i-1])
ans=''
for i in range(m):
    ans+=ans1[i]
print(ans)
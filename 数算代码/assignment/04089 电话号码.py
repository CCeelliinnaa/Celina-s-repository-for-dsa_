n=int(input())
ans=[]
for k in range(n):
    m=int(input())
    phonenum=[]
    for i in range(m):
        phonenum.append(input())
    phonenum.sort()
    flag=False
    for i in range(1,m):
        if len(phonenum[i-1])<=len(phonenum[i]):
            if phonenum[i][:len(phonenum[i-1])]==phonenum[i-1]:
                ans.append("NO")
                flag=True
                break
    if flag==False:
        ans.append("YES")
for i in ans:
    print(i)
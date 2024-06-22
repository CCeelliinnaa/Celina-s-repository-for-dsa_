s=input()
s=list(s)
stack=[]
cnt=0
ans=0
for i in s:
    if i=='(':
        stack.append(1)
    else:
        if stack:
            stack.pop()
            cnt+=2
        else:
            ans=max(ans,cnt)
            cnt=0
print(ans)
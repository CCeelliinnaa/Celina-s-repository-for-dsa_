s=list(input().split())
a=[]
for i in s:
    a.append(i)
ans=''
for i in range(len(s)-1):
    ans+=str(a.pop())+' '
ans+=str(a.pop())
print(ans)
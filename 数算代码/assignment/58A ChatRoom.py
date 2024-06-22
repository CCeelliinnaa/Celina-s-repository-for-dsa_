s=input()
s=list(s)
target=['h','e','l','l','o']
c=0
flag=False
for i in range(len(s)):
    if s[i]==target[c]:
        c+=1
    if c==5:
        flag=True
        break
if flag==True:
    print("YES")
else:
    print("NO")
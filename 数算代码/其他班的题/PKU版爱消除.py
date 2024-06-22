s=input()
s=list(s)
pku='PKU'
t=0
ans=[]
temp=[]
while s:
    x=s.pop(0)
    if t==3:
        temp=[]
        t=0
    if x==pku[t]:
        t+=1
        temp.append(x)
    else:
        t=0
        ans+=temp
        ans.append(x)
print(ans)
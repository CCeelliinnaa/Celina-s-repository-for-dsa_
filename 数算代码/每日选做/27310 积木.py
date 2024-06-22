n=int(input())
brick=[]
for i in range(4):
    l=list(input())
    brick.append(l)
words=[]
ans=[]
for i in range(n):
    w=list(input())
    tol=[]
    for j in range(len(w)):
        num=[]
        for k in range(4):
            if w[j]in brick[k]:
                num.append(k+1)
        tol.append(num)
    for j in range(4-len(w)):
        tol.append([1,2,3,4])
    flag=False
    for a in tol[0]:
       for b in tol[1]:
           for c in tol[2]:
               for d in tol[3]:
                   if a*b*c*d==24:
                       flag=True
                       break
    if flag:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)
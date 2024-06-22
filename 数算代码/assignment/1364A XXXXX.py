nC=int(input())
ans=[]
for i in range(nC):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    sum=0
    for i in l:
        sum+=i
    if sum%x!=0:
        ans.append(len(l))
    else:
        left=0
        right=0
        t=0
        for i in range(len(l)-1,-1,-1):
            t+=1
            if l[i]%x!=0:
                right=t
                break
        t=0
        for i in range(len(l)):
            t+=1
            if l[i]%x!=0:
                left=t
                break
        if min(right,left)==0:
            ans.append(-1)
        else:
            ans.append(len(l)-min(right,left))
for i in ans:
    print(i)
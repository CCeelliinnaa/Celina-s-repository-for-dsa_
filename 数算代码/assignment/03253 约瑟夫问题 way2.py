ans=[]
while(True):
    n,p,m=map(int,input().split())
    if n==m==p==0:
        break
    record=[]
    circle=[t for t in range(n)] ##0没用
    circle[0]=n
    cnt=0
    cur=p-1
    while(len(circle)>0):
        cur+=1
        cur=cur%len(circle)
        cnt+=1
        if cnt==m:
            cnt=0
            record.append(circle[cur])
            del circle[cur]
            cur-=1
    s=''
    for i in range(len(record)-1):
        s+=str(record[i])+','
    s+=str(record[len(record)-1])
    ans.append(s)
for i in ans:
    print(i)
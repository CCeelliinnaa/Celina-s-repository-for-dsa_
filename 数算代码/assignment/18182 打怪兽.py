from collections import defaultdict
nC=int(input())
ans=[]
for i in range(nC):
    n,m,b=map(int,input().split())
    store=[]
    for i in range(n):
        ti,xi=map(int,input().split())
        store.append([ti,xi])
    store.sort(key=lambda x:x[1],reverse=True)
    tim=set()
    for i in range(len(store)):
        tim.add(store[i][0])
    tim=list(tim)
    power={}
    total={}
    for t in tim:
        power[t]=0
        total[t]=0
    for i in store:
        if total[i[0]]<m:
            power[i[0]]+=i[1]
            total[i[0]]+=1
    cnt=0
    f=False
    tim.sort()
    for i in tim:
        cnt+=power[i]
        if cnt>=b:
            ans.append(i)
            f=True
            break
    if f==False:
        ans.append("alive")
for i in ans:
    print(i)
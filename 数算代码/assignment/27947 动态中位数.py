import heapq as h
n=int(input())
for i in range(n) :
    l=list(map(int,input().split()))
    q1=[] #小数堆
    q2=[] #大数堆
    h.heapify(q1)
    h.heapify(q2)
    siz1,siz2=0,0
    ans=[]
    for u in l:
        if siz2==0 :
            h.heappush(q2,u)
            siz2+=1
        else:
            v=h.heappop(q2)
            h.heappush(q2,v)
            if u>=v:
                h.heappush(q2,u)
                siz2+=1
            else:
                h.heappush(q1,-u)
                siz1+=1
        if siz1>siz2:
            u=-h.heappop(q1)
            siz1-=1
            h.heappush(q2,u)
            siz2+=1
        if siz2>siz1+1:
            u=h.heappop(q2)
            siz2-=1
            h.heappush(q1,-u)
            siz1+=1
        if siz2==siz1+1:
            u=h.heappop(q2)
            ans.append(u)
            h.heappush(q2,u)
    print(len(ans))
    print(" ".join(str(u) for u in ans))
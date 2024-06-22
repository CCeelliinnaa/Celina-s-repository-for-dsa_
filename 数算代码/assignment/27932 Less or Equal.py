n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
if k==0:
    if l[0]==1:
        print(-1)
    else:
        print(1)
elif n==1:
    print(l[0])
else:
    if l[k-1]>1000000000:
        print(-1)
    elif l[k-1]==l[k]:
        print(-1)
    else:
        print(l[k-1])
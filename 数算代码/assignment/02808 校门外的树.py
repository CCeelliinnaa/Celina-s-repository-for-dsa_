l,n=map(int,input().split())
tree=[1]*(l+1)
for i in range(n):
    start,end=map(int,input().split())
    tree[start:end+1]=[0]*(end-start+1)
cnt=0
for i in range(l+1):
    if tree[i]==1:
        cnt+=1
print(cnt)
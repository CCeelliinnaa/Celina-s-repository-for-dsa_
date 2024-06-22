n,m=map(int,input().split())
gra=[[] for i in range(n)]
award=[0 for i in range(n)]
inDegree=[0 for i in range(n)]
for i in range(m):
	a,b=map(int,input().split())
	gra[b].append(a)
	inDegree[a]+=1
q=[]
for i in range(n):
	if inDegree[i]==0:
		q.append(i)
		award[i]=100
while len(q)>0:
	u=q.pop(0)
	for v in gra[u]:
		inDegree[v]-=1
		award[v]=max(award[v],award[u]+1)
		if inDegree[v]==0:
			q.append(v)
total=sum(award)
print(total)
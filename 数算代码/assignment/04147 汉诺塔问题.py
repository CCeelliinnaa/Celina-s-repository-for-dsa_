n,a,b,c=input().split()
n=int(n)
ans=[]
def move(n,a,b,c):
    if n==1:
        ans.append(f"1:{a}->{c}")
    else:
        move(n-1,a,c,b)
        ans.append(f"{n}:{a}->{c}")
        move(n-1,b,a,c)
move(n,a,b,c)
for i in ans:
    print(i)
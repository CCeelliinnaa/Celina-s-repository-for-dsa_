n=int(input())
l=list(map(int,input().split()))
new_l=[]
for i in range(n):
    new_l.append([i+1,l[i]])
new_l.sort(key=lambda x:x[1])
shun=''
time=0
for i in range(n):
    shun+=str(new_l[i][0])+' '
    time+=new_l[i][1]*(n-1-i)
print(shun)
print(f"{time/n:.2f}")
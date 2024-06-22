cnt=[0]*100001
num=list(map(int,input().split()))
max=0
max_list=[]
for i in range(len(num)):
    cnt[num[i]]+=1
    if cnt[num[i]]==max:
        max_list.append(num[i])
    if cnt[num[i]]>max:
        max=cnt[num[i]]
        max_list=[]
        max_list.append(num[i])
max_list.sort()
ans=''
for i in range(len(max_list)):
    ans+=str(max_list[i])+' '
print(ans)
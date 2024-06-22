M,N=map(int,input().split())
word=list(map(int,input().split()))
store=[]
cnt=0
for i in range(N):
    if word[i] in store:
        pass
    else:
        if len(store)==M:
            store.pop(0)
            cnt+=1
            store.append(word[i])
        else:
            cnt+=1
            store.append(word[i])
print(cnt)
ans=[]
cnt=0
while(True):
    cnt+=1
    p,e,i,d=map(int,input().split())  #分别为体力周期、感情周期和智力周期，它们的周期长度分别为23天、28天和33天\
    p_date=[0]*(21253+d)
    e_date=[0]*(21253+d)
    i_date=[0]*(21253+d)
    if p==e==i==d==-1:
        break
    for k in range(p,-1,-23):
        p_date[k]=1
    for k in range(p,21253+d,23):
        p_date[k]=1
    for k in range(e,-1,-28):
        e_date[k]=1
    for k in range(e,21253+d,28):
        e_date[k]=1
    for k in range(i,-1,-33):
        i_date[k]=1
    for k in range(i,21253+d,33):
        i_date[k]=1
    for k in range(d+1,d+21253):
        if p_date[k]*e_date[k]*i_date[k]==1:
            ans.append(f'Case {cnt}: the next triple peak occurs in {k-d} days.')
            break
for i in ans:
    print(i)
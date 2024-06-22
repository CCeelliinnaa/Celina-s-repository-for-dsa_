n,a,b=map(int,input().split())
plant=list(map(int,input().split()))
ans=0
if n%2==0:
    a_cnt=0
    b_cnt=0
    cur_a=a
    cur_b=b
    for i in range(n//2):
        if plant[i]>cur_a:
            a_cnt+=1
            cur_a=a
        cur_a-=plant[i]
    for i in range(n-1,n//2-1,-1):
        if plant[i]>cur_b:
            b_cnt+=1
            cur_b=b
        cur_b-=plant[i]
    ans=a_cnt+b_cnt
else:
    a_cnt=0
    b_cnt=0
    cur_a=a
    cur_b=b
    for i in range(n//2):
        if plant[i]>cur_a:
            a_cnt+=1
            cur_a=a
        cur_a-=plant[i]
    for i in range(n-1,n//2,-1):
        if plant[i]>cur_b:
            b_cnt+=1
            cur_b=b
        cur_b-=plant[i]
    if plant[n//2]>max(cur_a,cur_b):
        ans=a_cnt+b_cnt+1
    else:
        ans=a_cnt+b_cnt
print(ans)
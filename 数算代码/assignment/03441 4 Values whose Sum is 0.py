def fourSumCount(A,B,C,D):
    count=0
    ab_sum={}
    for a in A:
        for b in B:
            ab_sum[a+b]=ab_sum.get(a+b,0)+1

    for c in C:
        for d in D:
            complement=-(c+d)
            if complement in ab_sum:
                count+=ab_sum[complement]
    return count

n=int(input())
A,B,C,D=[],[],[],[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
print(fourSumCount(A, B, C, D))
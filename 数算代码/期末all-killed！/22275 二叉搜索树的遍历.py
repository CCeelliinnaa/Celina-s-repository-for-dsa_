def ptop(pre):
    if len(pre)==1:
        return [pre[0]]
    if len(pre)==0:
        return []
    root=pre[0]
    left=[i for i in pre if i<root]
    right=[i for i in pre if i>root]
    return ptop(left)+ptop(right)+[root]

n=int(input())
pre=list(map(int,input().split()))
print(' '.join(map(str,ptop(pre))))
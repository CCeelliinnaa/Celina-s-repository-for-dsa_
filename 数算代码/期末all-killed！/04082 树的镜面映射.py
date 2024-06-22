from collections import defaultdict
n=int(input())
l=list(input().split())
level=1
tree=defaultdict(list)
for i in l:
    a=i[0]
    x=int(i[1])
    if a!='$':
        tree[level].append(a)
    if x==1:
        level-=1
    else:
        level+=1

ans=''
for l in tree.values():
    ans+=' '.join(reversed(l))+' '
print(ans)
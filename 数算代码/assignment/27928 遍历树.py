def traverse(root):
    ans=[]
    smaller=[x for x in tree[root] if x<root]
    greater=[x for x in tree[root] if x>root]
    for i in smaller:
        ans.extend(traverse(i))
    ans.append(root)
    for i in greater:
        ans.extend(traverse(i))
    return ans
        
n=int(input())
tree={}
is_not_root=[]
is_root=[]
for i in range(n):
    l=list(map(int,input().split()))
    node=l[0]
    child=l[1:]
    is_root.append(node)
    tree[node]=sorted(child)
    is_not_root+=sorted(child)
    
is_not_root=set(is_not_root)
is_not_root=list(is_not_root)

for x in is_root:
    if x not in is_not_root:
        root=x
        break

ans=traverse(root)
for i in ans:
    print(i)
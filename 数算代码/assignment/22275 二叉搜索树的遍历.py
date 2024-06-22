def pre_to_post(preorder):
    if not preorder:
        return []
    root=preorder[0]
    left_sub=[x for x in preorder if x<root]
    right_sub=[x for x in preorder if x>root]
    return pre_to_post(left_sub)+pre_to_post(right_sub)+[root]
    
n=int(input())
preorder=list(map(int,input().split()))
print(' '.join(map(str,pre_to_post(preorder))))
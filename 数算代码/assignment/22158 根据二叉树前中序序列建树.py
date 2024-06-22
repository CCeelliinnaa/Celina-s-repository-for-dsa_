def build_tree(preorder,inorder):
    if not preorder or not inorder:
        return []
    root_val=preorder[0]
    root_index=inorder.index(root_val)
    root=[]
    
    left_inorder=inorder[:root_index]
    right_inorder=inorder[root_index+1:]

    left_preorder=preorder[1:1+len(left_inorder)]
    right_preorder=preorder[1+len(left_inorder):]

    root.extend(build_tree(left_preorder,left_inorder))
    root.extend(build_tree(right_preorder,right_inorder))
    root.extend(root_val)
    return root

while True:
    try:
        preorder = input().strip()
        inorder = input().strip()
        postorder = build_tree(preorder, inorder)
        print(''.join(postorder))
    except EOFError:
        break
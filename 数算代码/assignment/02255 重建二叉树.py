def prein_to_post(pre,ino):
    if pre and ino:
        root=pre[0]
        i=ino.index(root)
        left_preorder=pre[1:1+i]
        right_preorder=pre[1+i:]
        left_inorder=ino[:i]
        right_inorder=ino[i+1:]
        return prein_to_post(left_preorder,left_inorder)+prein_to_post(right_preorder,right_inorder)+[root]
    else:
        return []

while True:
    try:
        pre,ino=input().split()
        post=prein_to_post(pre,ino)
        print(''.join(post))
    except EOFError:
        break
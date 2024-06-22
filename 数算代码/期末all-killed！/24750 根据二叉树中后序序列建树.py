def iptp(ino,poo):
    if len(poo)==1:
        return [poo[0]]
    if len(poo)==0:
        return []
    root=poo[-1]
    x=ino.index(root)
    left_ino=ino[:x]
    right_ino=ino[x+1:]
    left_poo=poo[:len(left_ino)]
    right_poo=poo[len(left_ino):len(poo)-1]
    return [root]+iptp(left_ino,left_poo)+iptp(right_ino,right_poo)

in_order=list(input())
post_order=list(input())
print(''.join(iptp(in_order,post_order)))
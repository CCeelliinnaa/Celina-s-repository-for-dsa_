def tree_swap(x,y):
    tree[loc[x][0]][loc[x][1]]=y
    tree[loc[y][0]][loc[y][1]]=x
    ##交换节点————只用把二者的父节点下位置交换即可！
    loc[x],loc[y]=loc[y],loc[x]

N=int(input())
for _ in range(N):
    n,m=map(int,input().split())
    tree={}
    loc=[[] for i in range(n)]
    for i in range(n):
        root,left,right=map(int,input().split())
        tree[root]=[left,right]
        loc[left],loc[right]=[root,0],[root,1]
    for i in range(m):
        deal=list(map(int,input().split()))
        if deal[0]==1:
            tree_swap(deal[1],deal[2])
        else:
            ans=deal[1]
            while tree[ans][0]!=-1:
                ans=tree[ans][0]
            print(ans)
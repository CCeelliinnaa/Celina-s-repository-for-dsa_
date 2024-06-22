# 第一种建树方法——class Treenode法
class Treenode():
    def __init__(self,num):
        self.num=num
        self.left=None
        self.right=None

def find_height(x,cnt=0):
    if x==None:
        return 0
    lc=x.left
    rc=x.right
    return max(find_height(lc),find_height(rc))+1
    
n=int(input())
node=[Treenode(i) for i in range(n+1)]
for i in range(1,n+1):
    l,r=map(int,input().split()) #建树
    if l!=-1:
        node[i].left=node[l]
    if r!=-1:
        node[i].right=node[r]
print(find_height(node[1]))
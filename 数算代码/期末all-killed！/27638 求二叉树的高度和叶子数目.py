class Treenode():
    def __init__(self):
        self.left=None
        self.right=None

def find_height(node):
    if node==None:
        return 0
    return max(find_height(node.left),find_height(node.right))+1

def leave_num(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 1
    return leave_num(node.left)+leave_num(node.right)
    

n=int(input())
node=[Treenode() for i in range(n)]
has_parent=[False for i in range(n)]
for i in range(n):
    l,r=map(int,input().split())
    if l!=-1:
        node[i].left=node[l]
        has_parent[l]=True
    if r!=-1:
        node[i].right=node[r]
        has_parent[r]=True
root=has_parent.index(False)
print(f"{find_height(node[root])-1} {leave_num(node[root])}")
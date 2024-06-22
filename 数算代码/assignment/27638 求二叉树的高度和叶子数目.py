class Treenode():
    def __init__(self):
        self.left=None
        self.right=None

def find_tree_height(node):
    if node==None:
        return -1
    return max(find_tree_height(node.left),find_tree_height(node.right))+1
def count_leef(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 1
    return count_leef(node.left)+count_leef(node.right)

n=int(input())
nodes=[Treenode() for i in range(n)]
has_parent=[False for i in range(n)]
for i in range(n):
    left,right=map(int,input().split())
    if left!=-1:
        nodes[i].left=nodes[left]  #类似nodes[i].left->nodes[left]
        has_parent[left]=True
    if right!=-1:
        nodes[i].right=nodes[right]
        has_parent[right]=True
        
root=nodes[has_parent.index(False)]
print(f"{find_tree_height(root)} {count_leef(root)}")
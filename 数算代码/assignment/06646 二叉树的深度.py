class Treenode():
    def __init__(self):
        self.left=None
        self.right=None

def find_tree_height(node):
    if node==None:
        return 0
    return max(find_tree_height(node.left),find_tree_height(node.right))+1

n=int(input())
nodes=[Treenode() for i in range(n+1)]
has_parent=[False for i in range(n+1)]
has_parent[0]=True
for i in range(1,n+1):
    left,right=map(int,input().split())
    if left!=-1:
        nodes[i].left=nodes[left]
        has_parent[left]=True
    if right!=-1:
        nodes[i].right=nodes[right]
        has_parent[right]=True
    
root_index=has_parent.index(False)
print(find_tree_height(nodes[root_index]))
class Treenode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
def insert(root,newvalue):
    if root==None:
        return Treenode(newvalue)
    elif newvalue<root.value:
        root.left=insert(root.left,newvalue)
    elif newvalue>root.value:
        root.right=insert(root.right,newvalue)
    return root  ##正常来说，只要非空，根节点是不会变的吧？用这么一个return只是为了方便记住root？
        
def level_order_traversal(root):
    queue=[root]
    traversal=[]
    while queue:
        node=queue.pop(0)
        traversal.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return traversal

l=list(map(int,input().split()))
l=list(dict.fromkeys(l))
root=None
for num in l:
    root=insert(root,num)
traversal=level_order_traversal(root)
print(' '.join(map(str, traversal)))
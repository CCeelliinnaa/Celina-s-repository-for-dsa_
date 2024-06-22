class Treenode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def build_tree(s):
    x=s.pop(0)
    if x=='.':
        return
    node=Treenode(x)
    node.left=build_tree(s)
    node.right=build_tree(s)
    return node

def order(node,pos): ## 0:前  1:中  2:后
    if node:
        sub=[order(nd,pos) for nd in (node.left,node.right)]
        sub.insert(pos,node.value)
        return ''.join(sub)
    return ''

pre=list(input())
root=build_tree(pre)
print(order(root,1))
print(order(root,2))
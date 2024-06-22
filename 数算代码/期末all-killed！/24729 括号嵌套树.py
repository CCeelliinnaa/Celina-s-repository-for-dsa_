class Treenode():
    def __init__(self,value):
        self.child=[]
        self.value=value

def build_tree(s): # A(B(E),C(F,G),D(H(I)))
    temp=[]
    node=None
    root=None
    for x in s:
        if x.isalpha():
            node=Treenode(x)
            if temp:
                temp[-1].child.append(node)
        if x=="(":
            if node:
                temp.append(node)
                node=None
        if x==")":
            if temp:
                root=temp.pop()
    return node if root==None else root

def pre_order_print(node):
    ans=[node.value]
    for i in node.child:
        ans+=pre_order_print(i)
    return ans

def post_order_print(node):
    ans=[]
    for i in node.child:
        ans+=post_order_print(i)
    return ans+[node.value]

s=input()
s=list(s)
root=build_tree(s)
print(''.join(pre_order_print(root)))
print(''.join(post_order_print(root)))
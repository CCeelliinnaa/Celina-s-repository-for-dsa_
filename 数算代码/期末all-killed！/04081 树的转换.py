class Treenode():
    def __init__(self,value):
        self.value=value
        self.child=[]

def find_height1(node):
    return 1+max([find_height1(nod) for nod in node.child],default=-1)

def  find_height2(node):
    return 1+max([find_height2(node.child[i])+i for i in range(len(node.child))],default=-1)

s=input()
s=list(s)
id=0
root=Treenode(0)
stack=[root]
for i in s:
    if i=='d':
        node=Treenode(id)
        stack[-1].child.append(node)
        stack.append(node)
        id+=1
    else:
        stack.pop()
print(f'{find_height1(root)} => {find_height2(root)}')
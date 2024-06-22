class Node:
    def __init__(self,value,child):
        self.value=value
        self.child=child
        
def generateTree():
    if (x:=s.pop(0))!='.':
        return Node(x,[generateTree() for i in range(2)])
    
def order(node,pos):
    if node: ##node是不是None
        sub=[order(nd,pos) for nd in node.child]
        sub.insert(pos,node.value)
        return ''.join(sub)
    return ''

s=list(input())
root=generateTree()
for i in range(1,3):
    print(order(root,i))
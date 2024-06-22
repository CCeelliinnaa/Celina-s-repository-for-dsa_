class treeNode:
    def __init__(self):
        self.child = []
        
    def beforeH(self):
        return 1+max([node.beforeH() for node in self.child],default=-1)
    def newH(self):
        return 1+max([node.newH()+i for i,node in enumerate(self.child)],default=-1)


def build_tree():
    cur=treeNode()
    while s and s.pop(0)=='d':
        cur.child.append(build_tree())
    return cur

s=list(input())
root=build_tree()
print(f"{root.beforeH()} => {root.newH()}")
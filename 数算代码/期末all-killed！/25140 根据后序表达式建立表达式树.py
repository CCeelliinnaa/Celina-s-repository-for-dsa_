class Treenode():
    def __init__(self,num):
        self.left=None
        self.right=None
        self.num=num

def build_tree(s):
    stack=[]
    for i in s:
        node=Treenode(i)
        if i.isupper():
            node.right=stack.pop()
            node.left=stack.pop()
        stack.append(node)
    return stack[0]

def level_print(root):
    queue=[root]
    ans=[]
    while queue:
        x=queue.pop(0)
        ans.append(x.num)
        if x.left!=None:
            queue.append(x.left)
        if x.right!=None:
            queue.append(x.right)
    return ans[::-1]

n=int(input())
out=[]
for i in range(n):
    s=input()
    s=list(s)
    root=build_tree(s)
    out.append(level_print(root))
for i in out:
    print(''.join(i))
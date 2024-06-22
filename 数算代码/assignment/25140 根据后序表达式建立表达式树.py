class Treenode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def build_tree(postfix):
    stack=[]
    for char in postfix:
        node=Treenode(char)
        if char.isupper():
            node.right=stack.pop()  ##注意left和right的顺序！
            node.left=stack.pop()
        stack.append(node)
    return stack[0]

def level_print(root):
    queue=[root]
    reversal=[]
    while queue:
        node=queue.pop(0)
        reversal.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return reversal[::-1]

n=int(input())
ans=[]
for i in range(n):
    postfix=input().strip()
    root=build_tree(postfix)
    ans.append(''.join(level_print(root)))
for i in ans:
    print(i)
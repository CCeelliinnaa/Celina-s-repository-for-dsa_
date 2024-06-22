class Treenode():
    def __init__(self,value):
        self.value=value
        self.leftchild=None
        self.rightchild=None
def build_tree(s):
    if len(s)==1:
        if '1' in s:
            return Treenode('I')
        else:
            return Treenode('B')

    if '0' in s and '1' in s:
        root=Treenode('F')
    elif '0' in s:
        root=Treenode('B')
    else:
        root=Treenode('I')
    root.leftchild=build_tree(s[:len(s)//2])
    root.rightchild = build_tree(s[len(s)//2:])
    return root

def post(root):
    if root.leftchild==None and root.rightchild==None:
        return [root.value]
    return post(root.leftchild)+post(root.rightchild)+[root.value]

N=int(input())
s=input()
root=build_tree(s)
ans=post(root)
a=''
for i in ans:
    a+=i
print(a)
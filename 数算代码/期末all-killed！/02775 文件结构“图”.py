class node():
    def __init__(self,name):
        self.name=name
        self.dir=[]
        self.file=[]

def print_tree(nod,level=0):
    indent='|     '*level
    print(indent+nod.name)
    for dirs in nod.dir:
        print_tree(dirs,level+1)
    for files in sorted(nod.file):
        print(indent+files)

datas=[]
setnum=1
temp=[]
while True:
    line=input()
    if line=='#':
        break
    if line=='*':
        datas.append(temp)
        temp=[]
    else:
        temp.append(line)
for data in datas:
    print(f'DATA SET {setnum}:')
    root=node('ROOT')
    stack=[root]
    for x in data:
        if x[0]=="d":
            nod=node(x)
            stack[-1].dir.append(nod)
            stack.append(nod)
        if x[0]=="f":
            stack[-1].file.append(x)
        if x==']':
            stack.pop()
    print_tree(root)
    if setnum<len(datas):
        print()
    setnum+=1
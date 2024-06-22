class Deque():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

N=int(input())
ans=[]
for k in range(N):
    n=int(input())
    d=Deque()
    for i in range(n):
        type,x=map(int,input().split())
        if type==1:
            d.addRear(x)
        if type==2:
            if x==0:
                d.removeFront()
            if x==1:
                d.removeRear()
    if d.size()==0:
        ans.append("NULL")
    else:
        a=''
        while(d.size()):
            a+=str(d.removeFront())+' '
        ans.append(a)
for i in ans:
    print(i)
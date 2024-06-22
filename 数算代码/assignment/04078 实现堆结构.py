class Binheap():
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
    
    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
    
    def percUp(self,i):
        while i//2>0:
            if self.heapList[i]<self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2
    
    def insert(self,k):
        self.heapList.append(k) 
        self.currentSize=self.currentSize+1 
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while(i*2)<=self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]>self.heapList[mc]:
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc
        
    def delMin(self):
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist): 
        i=len(alist)//2 ##从len//2开始，因为最后一层不需要percDown
        self.currentSize=len(alist) 
        self.heapList=[0]+alist[:] 
        while(i>0): 
            self.percDown(i) 
            i=i-1
            
n=int(input())
ans=[]
heap=Binheap()
for i in range(n):
    l=list(map(int,input().split()))
    if len(l)==1:
        ans.append(heap.delMin())
    else:
        heap.insert(l[1])
for i in ans:
    print(i)
ans=[]
def queen(seq,hang):
    if hang==8:
        ans.append(''.join([str(x+1) for x in seq]))
        return
    for i in range(8):
        for j in range(hang):
            if seq[j]==i or abs(seq[j]-i)==abs(j-hang):
                break ##！！！
        else: ##!!!
            seq[hang]=i
            queen(seq,hang+1)

n=int(input())
queen([None]*8,0)
for i in range(n):
    a=int(input())
    print(ans[a-1])
while True:
    try:
        n=list(input())
        head=n[:len(n)//2]
        if len(n)%2==0:
            tail=n[len(n)//2:len(n)]
        else:
            tail=n[len(n)//2+1:len(n)]
        tail.reverse()
        if head==tail or len(n)==1:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
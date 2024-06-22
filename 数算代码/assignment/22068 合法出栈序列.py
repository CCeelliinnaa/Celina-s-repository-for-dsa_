origin=input()
while True:
    try:
        out=input()
        stack=[]
        out=list(out)
        if len(origin)!=len(out):
            print("NO")
        else:
            l=list(origin)
            while(len(l)):
                stack.append(l.pop(0))
                while len(stack) and stack[-1]==out[0]:
                    out.pop(0)
                    stack.pop()
            if len(stack):
                print("NO")
            else:
                print("YES")
    except EOFError:
        break    
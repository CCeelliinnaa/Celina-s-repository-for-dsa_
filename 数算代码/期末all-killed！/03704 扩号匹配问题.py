while True:
    try:
        s=list(input())
        ans=[' ']*len(s)
        stack_left=[]
        stack_right=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack_left.append(i)
            elif s[i]==')':
                if stack_left:
                    stack_left.pop()
                else:
                    stack_right.append(i)
        for i in range(len(ans)):
            if i in stack_left:
                ans[i]='$'
            if i in stack_right:
                ans[i]='?'
        print(''.join(s))
        print(''.join(ans))
    except EOFError:
        break
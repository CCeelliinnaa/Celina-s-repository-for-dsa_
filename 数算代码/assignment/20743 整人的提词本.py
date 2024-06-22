s=input()
stack=[]
for i in range(len(s)):
    if s[i]==")":
        temp=[]
        while (a:=stack.pop())!="(":
            temp.append(a)
        stack.extend(temp)
    else:
        stack.append(s[i])
print(''.join(stack))
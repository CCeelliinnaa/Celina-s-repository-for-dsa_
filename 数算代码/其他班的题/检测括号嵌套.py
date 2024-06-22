s=input()
stack=[]
left=['(','[','{']
right=[')',']','}']
is_multi=False
correct=True
for i in s:
    if i in left:
        stack.append(left.index(i))
    elif i in right:
        if right[stack.pop()]==i:
            if stack:
                is_multi=True
        else:
            correct=False
            break
if correct:
    if is_multi:
        print('YES')
    else:
        print('NO')
else:
    print('ERROR')
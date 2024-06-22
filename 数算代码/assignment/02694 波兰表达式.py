from collections import deque
d=deque()
l=list(input().split())
l.reverse()
for i in l:
    if i!='+' and i!='-' and i!='*' and i!='/':
        i=float(i)
        d.append(i)
    if i=='+':
        a=d.pop()
        b=d.pop()
        d.append(a+b)
    if i=='-':
        a=d.pop()
        b=d.pop()
        d.append(a-b)
    if i=='*':
        a=d.pop()
        b=d.pop()
        d.append(a*b)
    if i=='/':
        a=d.pop()
        b=d.pop()
        d.append(a/b)
print(f'{d[0]:.6f}')
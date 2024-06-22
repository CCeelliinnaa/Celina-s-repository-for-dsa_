s=list(input().split('+'))
max=0
for i in range(len(s)):
    a=list(s[i].split('n^'))
    if a[0]=='':
        continue
    elif int(a[0])!=0 and int(a[1])>max:
        max=int(a[1])
print(f'n^{max}')
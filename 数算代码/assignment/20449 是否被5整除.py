def bin_to_int(s):
    t=0
    ans=0
    s=list(s)
    s.reverse()
    s=''.join(s)
    for i in s:
        x=int(i)
        ans+=x*2**t
        t+=1
    return ans%5==0

s=input()
temp=''
ans=''
for i in range(len(s)):
    temp+=s[i]
    t=bin_to_int(temp)
    if t:
        t=1
    else:
        t=0
    ans+=str(t)
print(ans)
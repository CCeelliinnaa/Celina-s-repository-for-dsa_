s=input()
s=s.lower()
s=list(s)
ans=''
for i in range(len(s)):
    if s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u' and s[i]!="y":
        ans+='.'+s[i]
print(ans)#
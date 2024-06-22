def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b

l=list(map(int,input().split()))
mother=1
son=0
for i in range(1,len(l),2):
    mother*=l[i]
for i in range(0,len(l),2):
    son+=l[i]*(mother//l[i+1])
while gcd(son,mother)!=1:
    g=gcd(son,mother)
    son=son//g
    mother=mother//g
print(f'{son}/{mother}')
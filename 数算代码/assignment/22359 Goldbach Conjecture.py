prime=[1]*10001
def find_prime():
    for i in range(2,10001):
        if prime[i]==1:
            for j in range(2*i,10001,i):
                prime[j]=0
find_prime()
prime[1]=0
n=int(input())
for i in range(2,n//2+1):
    if prime[i]==1 and prime[n-i]==1:
        print(f"{i} {n-i}")
        exit()
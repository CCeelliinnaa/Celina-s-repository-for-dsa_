n=int(input())
pairs=[i[1:-1] for i in input().split()] ##！！！！！！！！！！！！！！！！！！！
distance=[sum(map(int,i.split(','))) for i in pairs]
price=list(map(int,input().split()))
new_l=[]
xjb=[]
for i in range(n):
    new_l.append([distance[i]/price[i],price[i]])
    xjb.append(distance[i]/price[i])
xjb.sort()
if len(xjb)%2==0:
    xjb_middle=(xjb[len(xjb)//2-1]+xjb[len(xjb)//2])/2
else:
    xjb_middle=xjb[len(xjb)//2]
price.sort()
if len(price)%2==0:
    price_middle=(price[len(price)//2-1]+price[len(price)//2])/2
else:
    price_middle=price[len(price)//2]
cnt=0
for i in range(n):
    if new_l[i][0]>xjb_middle and new_l[i][1]<price_middle:
        cnt+=1
print(cnt)
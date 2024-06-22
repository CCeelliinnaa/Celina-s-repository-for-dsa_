n=int(input())
dic={}
for i in range(n):
    id,m,d=input().split()
    date=int(m)*100+int(d)
    dic.setdefault(date,[]).append(id)
for i in sorted(dic):
    id_list=dic[i]
    if len(id_list)>1:
        ans=''
        for j in id_list:
            ans+=str(j)+' '
        print(f'{i//100} {i%100} {ans}')
from collections import defaultdict
n=int(input())
dic=defaultdict(list)
for i in range(n):
    name,big=input().split('-')
    big_num=float(big[:-1])
    if big[-1]=="M":
        dic[name].append([big,float(big_num/1000)])
    else:
        dic[name].append([big,float(big_num)])
ans=[]
for name in sorted(dic):
    num=dic[name]
    num.sort(key=lambda x:x[1])
    ans_str=name+': '
    for i in range(len(num)-1):
        ans_str+=num[i][0]+', '
    ans_str+=num[-1][0]
    ans.append(ans_str)
for i in ans:
    print(i)
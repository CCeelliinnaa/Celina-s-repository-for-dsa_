from collections import defaultdict
ans=[]
n,x,y=map(int,input().split())
course_num=defaultdict(int)
score_total=defaultdict(int)
for i in range(n):
    course,stu,score=input().split()
    course_num[stu]+=1
    score_total[stu]+=int(score)
m=int(input())
for i in range(m):
    name=input()
    if course_num[name]>=x and score_total[name]>course_num[name]*y:
        ans.append('yes')
    else:
        ans.append('no')
for i in ans:
    print(i)
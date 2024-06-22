from collections import defaultdict
ans=[]
team_id=defaultdict(str)
t=int(input())
for i in range(t):
    members=list(map(int,input().split()))
    for x in members:
        team_id[x]=i
        
team_tail=['' for i in range(t)]
total_list=[]

while True:
    s=input()
    if s=="STOP":
        break
    if s[0]=="D":
        ans.append(total_list[0])
        if team_id[total_list[0]]=='':
            pass
        else:
            id=team_id[total_list[0]]
            if total_list[0]==team_tail[id]:
                team_tail[id]=''
        total_list.pop(0)
    else:
        new=int(s[8:])
        if team_id[new]=='':
            total_list.append(new)
        else:
            if team_tail[team_id[new]]=='':
                total_list.append(new)
                team_tail[team_id[new]]=new
            else:
                total_list.insert(total_list.index(team_tail[team_id[new]])+1,new)
                team_tail[team_id[new]]=new

for i in ans:
    print(i)
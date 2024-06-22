from collections import defaultdict, deque
from itertools import permutations

bucket=defaultdict(list)   ##词桶
for o in range(int(input())):
    word=input()
    for i in range(4):
        label=list(word)
        label[i]='_'
        bucket[''.join(label)].append(word)  ##把桶建好。
##我们有了类似bucket：=['a_bc':['adbc','aebc'.....] ,'ab_c':....]

graph=defaultdict(list)  ##根据桶来建图。
for words in bucket.values():
    for a, b in permutations(words, 2):  
    #words 是一个包含字符串的集合（或列表），permutations(words, 2)会生成所有 words 中两两元素的排列组合。
        graph[a].append(b)  ##互相加边

start,end=input().split()
q=deque([start])
pre=dict()
used=set(q)
def bfs():  ##bfs标程
    while q:
        word=q.popleft()
        for nex in graph[word]:
            if nex not in used:
                used.add(nex)
                pre[nex]=word  ##记录目前的词nex是从哪个词变过来的。
                if nex==end:
                    return True
                q.append(nex)
res=bfs()
if res:
    ans=[end]
    while ans[-1] in pre:
        ans.append(pre[ans[-1]])
    print(*ans[::-1]) ##!
else:
    print('NO')
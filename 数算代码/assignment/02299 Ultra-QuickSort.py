def merge_sort(l):
    if len(l)<=1:
        return l,0
    mid=len(l)//2
    left_half,count_left=merge_sort(l[:mid])
    right_half,count_right=merge_sort(l[mid:])
    merged_l,count_merge=merge(left_half, right_half)
    count=count_left+count_right+count_merge
    return merged_l,count

def merge(left,right):
    merged=[]
    count=0
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
            count+=len(left)-i
    merged+=left[i:]
    merged+=right[j:]
    return merged, count
ans=[]
while(True):
    n=int(input())
    if n==0:
        break
    l=[]
    for i in range(n):
        x=int(input())
        l.append(x)
    cnt=0
    sorted_l,cnt=merge_sort(l)
    ans.append(cnt)
for i in ans:
    print(i)
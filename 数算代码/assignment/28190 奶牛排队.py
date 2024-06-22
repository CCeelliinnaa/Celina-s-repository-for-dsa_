import bisect

n = int(input())
a = [0] * (n + 1)
sx, sn = [], []
ans, tx, tn = 0, 0, 0

for i in range(1, n + 1):
    a[i] = int(input())

for i in range(1, n + 1):
    while tn and a[sn[tn]] >= a[i]:
        tn -= 1
    while tx and a[sx[tx]] < a[i]:
        tx -= 1
    k = bisect.bisect_right(sn[1:tn+1], a[sx[tx]])
    if k != (tn + 1):
        ans = max(ans, i - sn[k] + 1)
    tn += 1
    sn.append(i)
    tx += 1
    sx.append(i)

print(ans)
n = int(input())
s=0
for _ in range(n):
    x=[int(i)for i in input().split()]
    bad=False
    for i in range(1,len(x)):
        if not (q:=x[i]-x[i-1]) or abs(q) > 3:
            bad=True
            break
    if not bad:
        rvs=x[:]
        rvs.reverse()
        srt=list(sorted(x))
        s+=(x==srt or rvs==srt)
print(s)

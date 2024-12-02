def safe(x):
    bad=False
    for i in range(1,len(x)):
        if not (q:=x[i]-x[i-1]) or abs(q) > 3:
            bad=True
            break
    if not bad:
        rvs=x[:]
        rvs.reverse()
        srt=list(sorted(x))
        return x==srt or rvs==srt
n = int(input())
s=0
for _ in range(n):
    x=[int(i)for i in input().split()]
    if safe(x):
        s+=1
        continue
    for i in range(len(x)):
        k=x[:]
        del k[i]
        if safe(k):
            s+=1
            break
print(s)

import math

disk=input()
num_blocks=math.ceil(len(disk)/2)
r=[[] for _ in range(num_blocks)]
free=[[] for _ in range(math.floor(len(disk)/2))]
start=0
for i, s in enumerate(disk):
    w=int(s)
    if i%2==0:
        r[i//2].append([start, start+w-1])
    else:
        free[i//2] = [start, start+w-1]
    start+=w


while free:
    nf=free[0]
    wf=nf[1]-nf[0]
    ri=-1
    ri_good=False
    while not ri_good:
        if r[ri][-1][0] > nf[0]:
            ri_good=True
        else:
            ri-=1
            if abs(ri)>len(r):
                free=None
                break
    if free is None: continue

    wr=r[ri][-1][1]-r[ri][-1][0]
    if wr<=wf:
        del r[ri][-1]
        r[ri].insert(0, [nf[0],nf[0]+wr])
        if wr==wf:
            del free[0]
        else:
            free[0][0]+=wr+1
    else:
        r[ri][-1][-1]-=wf+1
        r[ri].insert(0, free[0])
        del free[0]

print(
    sum(
        n*(u*(u+1) - (l-1)*l)//2
        for n, rng in enumerate(r)
        for l, u in rng
    )
)

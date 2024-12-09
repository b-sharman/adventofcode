import math

disk=input()
num_blocks=math.ceil(len(disk)/2)
r=[[] for _ in range(num_blocks)]
free=[[] for _ in range(math.floor(len(disk)/2))]
start=0
for i, s in enumerate(disk):
    w=int(s)
    [r,free][i%2][i//2] = [start, start+w-1]
    start+=w

for ri in range(len(r)-1, -1, -1):
    for fi, nf in enumerate(free):
        wf=nf[1]-nf[0]
        if r[ri][0] > nf[0] and (wr:=r[ri][1]-r[ri][0])<=wf:
            r[ri]=[nf[0],nf[0]+wr]
            if wr==wf:
                del free[fi]
            else:
                free[fi][0]+=wr+1
            break

print(
    sum(
        n*(u*(u+1) - (l-1)*l)//2
        for n, (l, u) in enumerate(r)
    )
)

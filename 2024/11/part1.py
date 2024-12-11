stones=list(map(int, input().split()))

for _ in range(25):
    offset=False
    for i, s in enumerate(stones):
        if offset:
            offset=False
            continue
        if s==0:
            stones[i] = 1
        elif (l:=len(str(s))) % 2 == 0:
            stones[i] = int(str(s)[:l//2])
            stones.insert(i+1, int(str(s)[l//2:]))
            offset=True
        else:
            stones[i] = s * 2024
print(len(stones))

stones={int(x): 1 for x in input().split()}

for _ in range(75):
    orig=dict(stones)
    for k, v in tuple(stones.items()):
        if k==0:
            result = (1,)
        elif (l:=len(str(k))) % 2 == 0:
            result = (int(str(k)[:l//2]), int(str(k)[l//2:]))
        else:
            result = (k * 2024,)
        for r in result:
            if r in stones:
                stones[r] += v
            else:
                stones[r] = v
    for k, v in orig.items():
        stones[k] -= v
print(sum(stones.values()))

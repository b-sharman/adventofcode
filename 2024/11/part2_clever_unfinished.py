from collections import defaultdict

def calc(stone):
    global steps

    d = defaultdict(int, {stone: 1})
    for i in range(25):
        print(i, dict(d))
        for k, v in tuple(d.items()):
            # if k in steps:
            if False:
                d[k] += 1
            else:
                del d[k]
                if k==0:
                    result = (1,)
                elif (l:=len(str(k))) % 2 == 0:
                    result = (int(str(k)[:l//2]), int(str(k)[l//2:]))
                else:
                    result = (k * 2024,)
                for r in result:
                    d[r] += v
        steps[stone].append(d)
    return d

def expand(s):
    return sum(expand(steps[k[0]][k[1]])*v if type(k) is tuple else v for k, v in calc(s).items())

stones=[int(x) for x in input().split()]
steps=defaultdict(list)
print(sum(map(expand, stones)))

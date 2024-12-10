def dfs(m, pt, prev=None):
    c=m[pt[1]][pt[0]]
    if prev is not None and ord(c) - ord(prev) != 1:
        return 0
    if c == "9":
        return 1

    sm=0
    if pt[0] > 0:
        sm+=dfs(m, (pt[0]-1, pt[1]), prev=c)
    if pt[0] < len(m[0])-1:
        sm+=dfs(m, (pt[0]+1, pt[1]), prev=c)
    if pt[1] > 0:
        sm+=dfs(m, (pt[0], pt[1]-1), prev=c)
    if pt[1] < len(m)-1:
        sm+=dfs(m, (pt[0], pt[1]+1), prev=c)

    return sm

m=[]
trhds=[]
for y in range(int(input())):
    m.append(row := input())
    for x, c in enumerate(row):
        if c == "0":
            trhds.append((x, y))

print(sum(dfs(m, t) for t in trhds))

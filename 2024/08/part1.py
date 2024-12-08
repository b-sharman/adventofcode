locs={}
for y in range(height:=int(input())):
    for x, c in enumerate(row:=input()):
        if c != '.':
            if c in locs:
                locs[c].append((x, y))
            else:
                locs[c] = [(x, y)]
    width=len(row)

unq=set()
for n in locs.values():
    for i, m in enumerate(n):
        for j in range(i):
            o=n[j]
            diff = (o[0]-m[0], o[1]-m[1])
            pts=(
                (o[0]-diff[0],o[1]-diff[1]),
                (o[0]+diff[0],o[1]+diff[1]),
                (m[0]-diff[0],m[1]-diff[1]),
                (m[0]+diff[0],m[1]+diff[1]),
            )
            unq|=set(
                pt
                for pt in pts
                if pt!=o and pt!=m and pt[0]>=0 and pt[0]<width and pt[1]>=0 and pt[1]<height
            )
print(len(unq))

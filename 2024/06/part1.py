markers=set()
pos=None
width=None
for y in range(height:=int(input())):
    row=input()
    width=len(row)
    for x, c in enumerate(row):
        if c == "^":
            pos=(x, y)
        if c == "#":
            markers.add((x, y))

diridx=0
right=((0,-1), (1,0), (0,1), (-1,0))
visited=set()
while True:
    visited.add(tuple(pos))
    dir=right[diridx]
    newpos=(pos[0]+dir[0],pos[1]+dir[1])
    if newpos in markers:
        diridx=(diridx+1)%len(right)
        continue
    pos=newpos
    if pos[0] < 0 or pos[0] >= width or pos[1] < 0 or pos[1] >= height:
        break
print(len(visited))

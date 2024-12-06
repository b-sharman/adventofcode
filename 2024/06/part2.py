start_markers=set()
startpos=None
width=None
for y in range(height:=int(input())):
    row=input()
    width=len(row)
    for x, c in enumerate(row):
        if c == "^":
            startpos=(x, y)
        if c == "#":
            start_markers.add((x, y))

attempted_locations=set() # where have we tried adding obstacles?
sm=0
right=((0,-1), (1,0), (0,1), (-1,0))
tried_all = False
while not tried_all:
    diridx=0
    markers=set(start_markers)
    pos=startpos
    to_visit=dict()
    tried_this_time=False
    while True:
        dir=right[diridx]
        newpos=(pos[0]+dir[0],pos[1]+dir[1])

        if newpos in to_visit and dir in to_visit[newpos]:
            sm+=1
            break

        if newpos in markers:
            diridx=(diridx+1)%len(right)
            continue

        if not tried_this_time and newpos not in attempted_locations:
            attempted_locations.add(newpos)
            markers.add(newpos)
            tried_this_time=True
            continue

        if newpos in to_visit:
            to_visit[newpos].add(dir)
        else:
            to_visit[newpos]={dir}
        pos=newpos
        if pos[0] < 0 or pos[0] >= width or pos[1] < 0 or pos[1] >= height:
            break

    tried_all = not tried_this_time
print(sm)

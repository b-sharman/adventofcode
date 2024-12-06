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
tried_all = False
while not tried_all:
    print("\nnew try")
    diridx=0
    markers=set(start_markers)
    pos=startpos
    pos_after_turn=startpos
    right=((0,-1), (1,0), (0,1), (-1,0))
    turned_last_time=False
    vecs=dict()
    visited=dict()
    tried_this_time=False
    while True:
        dir=right[diridx]
        newpos=(pos[0]+dir[0],pos[1]+dir[1])

        if newpos in visited and visited[newpos]==dir:
            print("infinite loop reached")
            sm+=1
            break

        if newpos in markers:
            diridx=(diridx+1)%len(right)
            vecs[pos_after_turn]=pos
            print(f"finished line from {pos_after_turn} to {pos}")
            pos_after_turn=pos
            turned_last_time=True
            continue

        # if the current position lies on an existing vector
        on_prev_line=False
        if not turned_last_time:
            for start, end in vecs.items():
                if (pos[0] == start[0] and pos[1]>=min(start[1],end[1]) and pos[1]<=max(start[1],end[1])) \
                    or (pos[1] == start[1] and pos[0]>=min(start[0],end[0]) and pos[0]<=max(start[0],end[0])):
                    print(f"on prev line at {pos}")
                    on_prev_line=True
                    break
        if not tried_this_time and on_prev_line and newpos != startpos and newpos not in attempted_locations:
            # would adding an obstacle at newpos create an infinite loop?
            attempted_locations.add(newpos)
            markers.add(newpos)
            tried_this_time=True
            print(f"trying new marker at {newpos}")
            turned_last_time=False # not sure this is necessary
            continue

        visited[pos]=dir
        pos=newpos
        if pos[0] < 0 or pos[0] >= width or pos[1] < 0 or pos[1] >= height:
            break

        turned_last_time=False
    tried_all = not tried_this_time
print(sm)

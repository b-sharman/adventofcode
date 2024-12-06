markers=set()
startpos=None
width=None
for y in range(height:=int(input())):
    row=input()
    width=len(row)
    for x, c in enumerate(row):
        if c == "^":
            startpos=(x, y)
        if c == "#":
            markers.add((x, y))

sm=0
for y in range(height):
    for x in range(width):
        newm = (x, y)
        if newm in markers or newm==startpos:
            continue
        markers.add(newm)

        diridx=0
        pos=startpos
        right=((0,-1), (1,0), (0,1), (-1,0))
        visited=dict()
        while True:
            dir=right[diridx]
            newpos=(pos[0]+dir[0],pos[1]+dir[1])
            if newpos in visited and visited[newpos]==dir:
                # print("infinite loop reached")
                sm+=1
                break
            if newpos in markers:
                # print(f"{newpos=}, {pos=}")
                diridx=(diridx+1)%len(right)
            elif newpos[0] < 0 or newpos[0] >= width or newpos[1] < 0 or newpos[1] >= height:
                break
            else:
                visited[pos]=dir
                # print(f"visited {pos}")
                pos=newpos

        markers.remove(newm)
print(sm)

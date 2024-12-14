import math, re

with open("14") as f:
    pzin=f.read().strip().split("\n")
width, height = 101, 103 # 11, 7
robots = [map(int, re.findall(r"-?\d+", line)) for line in pzin]
endposes=[((px+vx*100)%width, (py+vy*100)%height) for px, py, vx, vy in robots]
quads=[0]*4
for epx, epy in endposes:
    if epx < width//2:
        if epy < height//2:
            quads[1] += 1
        elif epy > height//2:
            quads[2] += 1
    elif epx > width//2:
        if epy < height//2:
            quads[0] += 1
        elif epy > height//2:
            quads[3] += 1
print(math.prod(quads))

with open("13") as f:
    pzs=f.read().strip().split("\n\n")
sm=0
for pz in pzs:
    lines = pz.split("\n")
    ax,ay=(int(s[2:]) for s in lines[0].split(": ")[1].split(", "))
    bx,by=(int(s[2:]) for s in lines[1].split(": ")[1].split(", "))
    x,y=(int(s[2:])+10000000000000 for s in lines[2].split(": ")[1].split(", "))

    a=(bx*y-by*x)/(bx*ay-by*ax)
    b=(ax*y-ay*x)/(ax*by-ay*bx)

    if a==int(a) and b==int(b):
        sm+=3*a+1*b

print(int(sm))

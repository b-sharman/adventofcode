with open("13") as f:
    pzs=f.read().strip().split("\n\n")
sm=0
for pz in pzs:
    lines = pz.split("\n")
    xs,ys=lines[0].split(": ")[1].split(", ")
    ax=int(xs[2:])
    ay=int(ys[2:])
    xs,ys=lines[1].split(": ")[1].split(", ")
    bx=int(xs[2:])
    by=int(ys[2:])
    xprz,yprz=lines[2].split(": ")[1].split(", ")
    x=int(xprz[2:])+10000000000000
    y=int(yprz[2:])+10000000000000

    a=(bx*y-by*x)/(bx*ay-by*ax)
    b=(ax*y-ay*x)/(ax*by-ay*bx)

    if a>=0 and b>=0 and a==int(a) and b==int(b):
        sm+=3*a+1*b

print(int(sm))

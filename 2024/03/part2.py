import re

s=input()
pat=re.compile(r"(?:mul\((\d+),(\d+)\))|(?:(don't)|(do)\(\))")
sm=0
enabled=True
for t in pat.findall(s):
    mul=False
    k=1
    for x in t:
        match x:
            case "": pass
            case "do": enabled=True
            case "don't": enabled=False
            case _:
                mul=True
                k*=int(x)
    sm+=enabled*mul*k
print(sm)

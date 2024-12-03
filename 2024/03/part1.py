import re

s=input()
pat=re.compile(r"mul\((\d+),(\d+)\)")
sm=0
for t in pat.findall(s):
    k=1
    for n in t: k*=int(n)
    sm+=k
print(sm)

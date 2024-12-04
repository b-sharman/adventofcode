import re

pat = re.compile("(M.S.A.M.S)|(S.S.A.M.M)|(M.M.A.S.S)|(S.M.A.S.M)")

grid=[input()for _ in range(int(input()))]
s=0

for y in range(len(grid)-2):
    for x in range(len(grid[0])-2):
        sr=grid[y][x:x+3]
        for i in (1,2):
            sr+=grid[y+i][x:x+3]
        s+=pat.fullmatch(sr)is not None

print(s)

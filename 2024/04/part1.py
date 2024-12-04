def cis(s):
    r=0
    while len(s) >= 4:
        r+=s[:4]=='XMAS'
        s=s[1:]
    return r

def straight(grid):
    s=0
    for row in grid:
        # forward
        s+=cis(row)
        # backward
        s+=cis(row[::-1])
    return s

grid=[input()for _ in range(int(input()))]
s=0

s+=straight(grid)

# swap rows and cols
rvsg=[""]*len(grid[0])
for row in grid:
    for i, c in enumerate(row):
        rvsg[i] += c
s+=straight(rvsg)

# southeast
for y in range(len(grid)-3):
    for x in range(len(grid[0])-3):
        s+=cis("".join(grid[y+i][x+i] for i in range(4)))

# southwest
for y in range(len(grid)-3):
    for x in range(3,len(grid[0])):
        s+=cis("".join(grid[y+i][x-i] for i in range(4)))

# northeast
for y in range(3,len(grid)):
    for x in range(len(grid[0])-3):
        s+=cis("".join(grid[y-i][x+i] for i in range(4)))

# northwest
for y in range(3,len(grid)):
    for x in range(3,len(grid[0])):
        s+=cis("".join(grid[y-i][x-i] for i in range(4)))

print(s)

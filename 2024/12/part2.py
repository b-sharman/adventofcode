def bfs(x, y, visited):
    plant=map[y][x]
    pts=set()

    to_search=[]
    conditions=(True, x>0, x<width-1, y>0, y<height-1)
    dirs=((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
    for c, d in zip(conditions, dirs):
        newpt = (x+d[0], y+d[1])
        if c and map[newpt[1]][newpt[0]] == plant:
            if newpt not in visited:
                pts.add(newpt)
                visited.add(newpt)
                if newpt != (x, y):
                    to_search.append(newpt)

    for ts in to_search:
        pts |= bfs(*ts, visited)

    return pts

map=[input() for _ in range(int(input()))]
width=len(map[0])
height=len(map)

ans=0
visited = set()
for y in range(height):
    for x in range(width):
        if (x, y) not in visited:
            print(f"\nchecking out ({x}, {y}) = '{map[y][x]}'")
            pts = bfs(x, y, set())
            visited |= pts

            sides = 0
            prev_xbreaks = []
            for ri in sorted(set(pt[1] for pt in pts)):
                xs = [pt[0] for pt in pts if pt[1] == ri]
                if not xs:
                    continue
                xs.sort()
                xbreaks = []
                last_top = xs[0]-2
                last_bot = xs[0]-2
                for i, x_ in enumerate(xs):
                    # left
                    if i==0 or xs[i-1] != x_-1:
                        sides += (x_,0) not in prev_xbreaks
                        xbreaks.append((x_, 0))
                    # right
                    if i==len(xs)-1 or xs[i+1] != x_+1:
                        sides += (x_,1) not in prev_xbreaks
                        xbreaks.append((x_, 1))
                    # top
                    if (x_,ri-1) not in pts:
                        sides += last_top != x_-1
                        last_top = x_
                    # bottom
                    if (x_,ri+1) not in pts:
                        sides += last_bot != x_-1
                        last_bot = x_
                prev_xbreaks = xbreaks
            print("sides:", sides)
            ans += len(pts) * sides

print(ans)

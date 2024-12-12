def bfs(x, y, visited, perimeter=0):
    plant=map[y][x]
    pts=set()

    to_search=[]
    conditions=(True, x>0, x<width-1, y>0, y<height-1)
    dirs=((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
    for c, d in zip(conditions, dirs):
        newpt = (x+d[0], y+d[1])
        if c and map[newpt[1]][newpt[0]] == plant:
            if newpt == (x, y):
                perimeter+=4
            else:
                perimeter-=1
            if newpt not in visited:
                pts.add(newpt)
                visited.add(newpt)
                if newpt != (x, y):
                    to_search.append(newpt)

    for ts in to_search:
        new_pts, new_perimeter = bfs(*ts, visited, perimeter=perimeter)
        pts |= new_pts
        perimeter = new_perimeter

    return pts, perimeter

map=[input() for _ in range(int(input()))]
width=len(map[0])
height=len(map)

ans=0
visited = set()
for y in range(height):
    for x in range(width):
        if (x, y) not in visited:
            print(f"checking out ({x}, {y}) = '{map[y][x]}'")
            pts, perimeter = bfs(x, y, set())
            print("has points:", pts)
            print("and perimeter:", perimeter)
            ans += len(pts) * perimeter
            visited |= pts
print(ans)

n = int(input())
left = []
right = []
for _ in range(n):
    l,r=(int(x) for x in input().split())
    left.append(l)
    right.append(r)
print(sum(l*right.count(l) for l in left))
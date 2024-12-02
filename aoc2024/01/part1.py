n = int(input())
left = []
right = []
for _ in range(n):
    l,r=(int(x) for x in input().split())
    left.append(l)
    right.append(r)
left.sort()
right.sort()
print(sum(abs(l-r) for l,r in zip(left,right)))

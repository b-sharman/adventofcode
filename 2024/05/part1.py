rules=[tuple(int(x)for x in input().split("|")) for _ in range(int(input()))]
updates=[
    {int(x):i for i,x in enumerate(input().split(","))}
    for _ in range(int(input()))
]
sm=0
for u in updates:
    valid=True
    for rule in rules:
        if rule[0] in u and rule[1] in u and u[rule[0]] > u[rule[1]]:
            valid=False
            break
    if valid:
        sm+=tuple(u.keys())[len(u)//2]
print(sm)

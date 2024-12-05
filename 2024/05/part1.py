n=int(input())
rules=[tuple(int(x)for x in input().split("|")) for _ in range(n)]
m=int(input())
updates=[]
for _ in range(m):
    updates.append({int(x):i for i,x in enumerate(input().split(","))})
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

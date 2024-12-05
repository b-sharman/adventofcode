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
    if valid: continue

    # the update is incorrectly ordered; do insertion sort based on the rules
    while not valid:
        valid=True
        for rule in rules:
            if rule[0] in u and rule[1] in u and u[rule[0]] > u[rule[1]]:
                tmp=u[rule[0]]
                u[rule[0]]=u[rule[1]]
                u[rule[1]]=tmp
                valid=False
                break
    sm+={i:n for n,i in u.items()}[len(u)//2]
print(sm)

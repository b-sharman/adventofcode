eqs=[(int((x:=input().split(":"))[0]), list(map(int, filter(bool, x[1].split(" "))))) for _ in range(int(input()))]
sm=0
for rslt, nums in eqs:
    c=[['+'], ['*']]
    while not all(len(q)==len(nums)-1 for q in c):
        x=c.pop(0)
        c.append(x+['+'])
        c.append(x+['*'])
    for p in c:
        b=nums[0]
        for i, l in enumerate(p):
            if l=='+': b+=nums[i+1]
            elif l=='*': b*=nums[i+1]
        if b==rslt:
            sm+=rslt
            break
print(sm)

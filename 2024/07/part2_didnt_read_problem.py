eqs=[(int((x:=input().split(":"))[0]), list(map(int, filter(lambda q: q, x[1].split(" "))))) for _ in range(int(input()))]
sm=0
for rslt, nums in eqs:
    c=[['+'], ['*'], ['||']]
    while not all(len(q)==len(nums)-1 for q in c):
        x=c.pop(0)
        c.append(x+['+'])
        c.append(x+['*'])
        c.append(x+['||'])
    for p in c:
        print()
        print(rslt)
        print(nums)
        print(p)
        complete=[nums[0]]
        offset=0
        for i, l in enumerate(p):
            if l=='||':
                complete[-1]=int(str(complete[-1])+str(nums[i+1]))
                offset+=1
            else:
                complete.append(l)
                complete.append(nums[i+1])
        print(complete)
        b=complete[0]
        op=None
        for i, r in enumerate(complete[1:]):
            if i%2:
                if op=='+': b+=r
                elif op=='*': b*=r
                print(b)
            else:
                op=r
                print(f'{op=}')
        if b==rslt:
            print(f"satisfied {rslt}")
            sm+=rslt
            break
print(sm)

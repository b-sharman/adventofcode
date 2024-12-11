def calc(stone, dist, orig=None):
    global steps

    if type(stone) is not int:
        print(f"uh oh, calc received 'stone' {stone}")
        exit()

    if dist < 0:
        print(f"uh oh, dist is {dist}")
        exit()

    if dist == 0:
        return stone

    if stone in steps:
        if dist < len(steps[stone]):
            return steps[stone][dist]
        # else:
        #     cd = steps[stone][-1]
        #     if type(cd) is int:
        #         to_op =(cd,)
        #     else: 
        #         to_op = (cd[0], cd[1])
        #     return sum(t + calc(t, dist-len(steps[stone])+1) for t in to_op)

    if stone==0:
        result = 1
    elif (l:=len(str(stone))) % 2 == 0:
        result = (int(str(stone)[:l//2]), int(str(stone)[l//2:]))
    else:
        result = stone * 2024
    if orig is None:
        steps[stone] = [result]
        next_orig = stone
    else:
        steps[orig].append(result)
        next_orig = orig
    print(f"{result=}")
    if type(result) is int:
        return calc(result, dist-1, orig=next_orig)
    else:
        return sum(calc(rx, dist-1, orig=next_orig) for rx in result)

# current idea: change recursion to queue to mitigate complications arising when you wanna return the result of calc() on each member of a tuple
# or who knows, maybe the brute force way will be done when I wake up lol

stones=[int(x) for x in input().split()]
steps=dict()
# change 2nd argument of calc to 75 when testing is complete
print(sum(map(lambda s: 1 + (type(calc(s, 75)) is not int), stones)))

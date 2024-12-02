elves = []
s=0
while True:
    try:
        s = 0
        while True:
            try:
                s += int(input())
            except ValueError:
                break
        elves.append(s)
    except EOFError:
        elves.append(s)
        break
elves.sort()
print(sum(elves[-3:]))

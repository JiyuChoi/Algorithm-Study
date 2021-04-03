n, m = map(int, input().split())
people = sorted(list(map(int, input().split())))

cnt = 0

while people:
    if len(people)==1:
        cnt += 1
        break
    if people[0] + people[-1] > m:
        people.pop()
        cnt += 1
    else:
        people.pop()
        people.pop(0)
        cnt += 1

print(cnt)
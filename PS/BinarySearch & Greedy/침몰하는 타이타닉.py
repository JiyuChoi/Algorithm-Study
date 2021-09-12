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

# 9/11
n, m = map(int, input().split())
p = sorted(list(map(int, input().split())))
cnt = 0

s, e = 0, n-1
while s <= e:
    if p[s] + p[e] > m:
        e -= 1
        cnt += 1
    else:
        s += 1
        e -= 1
        cnt += 1

print(cnt)
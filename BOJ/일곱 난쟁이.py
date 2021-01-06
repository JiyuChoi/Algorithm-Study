# index를 저장하는 풀이
h = [int(input()) for i in range(9)]
total = sum(h) - 100

for i in range(9):
    for j in range(i+1, 9):
        if h[i] + h[j] == total:
            save = [i, j]

del h[save[0]]
del h[save[1]-1]

h.sort()

for n in h:
    print(n)


# flag를 이용한 풀이 (중간에 break하므로 시간 단축)
p = [int(input()) for _ in range(9)]
tot = sum(p) - 100
flag = False

for i in range(8):
    for j in range(i+1, 9):
        if p[i] + p[j] == tot:
            flag = True
            break

    if flag == True:
        break

del p[i]
del p[j-1]

h.sort()

for i in p:
    print(i)
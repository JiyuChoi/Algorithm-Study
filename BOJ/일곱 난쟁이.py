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
n = int(input())

for x in range(1, n+1):
    m = 0
    for s in str(x):
        if s in ('3', '6', '9'):
            m += 1
    if m > 0:
        print(m*'-', end=" ")
    else:
        print(x, end=" ")
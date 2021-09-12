t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    p = [[i + 1 for i in range(14)]]
    for i in range(k):
        tmp = []
        for j in range(n):
            tmp.append(sum(p[i][:j+1]))
        p.append(tmp)
    print(p[-1][-1])
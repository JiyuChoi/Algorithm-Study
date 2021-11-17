m = int(input())
cup = [i for i in range(4)]
for _ in range(m):
    x, y = map(int, input().split())
    a = cup.index(x)
    b = cup.index(y)
    cup[a], cup[b] = cup[b], cup[a]
print(cup[1])
import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [i for i in range(n+1)]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[a] = b

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

for _ in range(m):
    k, a, b = map(int, sys.stdin.readline().rstrip().split())
    if k == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]

maxdis = float("-inf")

for i in range(1, n-1):
    bdis = abs(cp[i][0]-cp[i+1][0]) + abs(cp[i][1]-cp[i+1][1]) + abs(cp[i-1][0]-cp[i][0]) + abs(cp[i-1][1]-cp[i][1])
    jumpdis = abs(cp[i-1][0]-cp[i+1][0]) + abs(cp[i-1][1]-cp[i+1][1])
    maxdis = max(maxdis, bdis-jumpdis)

totaldis = 0
for i in range(1, n):
    totaldis += abs(cp[i][0]-cp[i-1][0]) + abs(cp[i][1]-cp[i-1][1])
print(totaldis-maxdis)
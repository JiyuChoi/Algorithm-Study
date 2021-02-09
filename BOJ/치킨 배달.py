from itertools import combinations
import sys
N, M = map(int, input().split())
# 전체 맵 입력 받기
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken, home = [], []
ans = []


for i in range(N):
    for j in range(N):
        # 치킨가게 좌표 저장
        if city[i][j] == 2:
            chicken.append((i, j))
        # 집 좌표 저장
        if city[i][j] == 1:
            home.append((i, j))

#combination 풀이
for ch in combinations(chicken, M):
    d = 0
    for i in home:
        # 치킨 거리 계산
        d += min([abs(i[0]-j[0])+abs(i[1]-j[1]) for j in ch])
    ans.append(d)

print(min(ans))

# DFS 풀이
def dfs(s, l):
    global min_v
    if l == M:
        res = 0
        for h in home:
            dis = float("inf")
            for k in ch:
                dis = min(dis, abs(h[0]-k[0]) + abs(h[1]-k[1]))
            res += dis
        if res < min_v:
            min_v = res
    else:
        for i in range(s, len(chicken)):
            ch[l] = chicken[i]
            s = i+1
            dfs(s, l+1)

min_v = float("inf")
ch = [0]*M
dfs(0, 0)

print(min_v)

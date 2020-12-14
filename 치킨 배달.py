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
            chicken.append([i, j])
        # 집 좌표 저장
        if city[i][j] == 1:
            home.append([i, j])

for ch in combinations(chicken, M):
    d = 0
    for i in home:
        # 치킨 거리 계산
        d += min([abs(i[0]-j[0])+abs(i[1]-j[1]) for j in ch])
    ans.append(d)

print(min(ans))
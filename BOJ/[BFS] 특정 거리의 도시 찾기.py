# 그래프에서 모든 간선의 비용이 동일할 때는 BFS을 이용해 최단거리 찾기 가능

import sys
from collections import deque

# n, m, k, x 값 입력 받
n, m, k, x = map(int, sys.stdin.readline().split())

# 최단 거리 리스트 초기화
dis = [-1]*(n+1)
dis[x] = 0

# 노드 간 연결 리스트
link = [[] for _ in range(n+1)]

# 모든 도로 정보 입력 받기
# 여기서 x 쓰는 것 주의!
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    link[i].append(j)

# BFS 수행
d = deque([x])
while d:
    now = d.popleft()
    # 현재 노드에 연결된 노드를 확인
    for next in link[now]:
        # 방문하지 않았으면
        if dis[next] == -1:
            # 최단 거리 기록
            dis[next] = dis[now] + 1
            d.append(next)


flag = False
# 최단거리가 k인 노드를 오름차순으로 출력
for i in range(1, n+1):
    if dis[i] == k:
        print(i)
        flag = True

# 만약 최단거리가 K인 노드가 없다면, -1 출력
if not flag:
    print(-1)
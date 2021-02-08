from collections import deque

# 위치 입력 받기
n, k = map(int, input().split())
max_v = 100001
dis = [0]*max_v

d = deque()
d.append(n)

while d:
    now = d.popleft()
    # 현재 위치가 도착지점과 같은 경우 break
    if now == k:
        print(dis[now])
        break

    # -1, +1, *2의 경우를 나누어 계산
    for next in (now-1, now+1, 2*now):
        # 범위 내에 있고, 중복되지 않은 경우
        if 0 <= next < max_v and dis[next] == 0:
            d.append(next)
            dis[next] = dis[now] + 1

from collections import deque

n = int(input())

q = deque()
max_s = 1001
time = [[-1] * max_s for _ in range(max_s)]

q.append((1, 0))
time[1][0] = 0

while q:
    s, c = q.popleft()

    if time[s][s] == -1: # 클립보드 저장
        time[s][s] = time[s][c] + 1
        q.append((s, s))
    if s+c <= n and time[s+c][c] == -1: # 클립보드 붙여넣기
        time[s+c][c] = time[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and time[s-1][c] == -1: # 이모티콘 삭제
        time[s-1][c] = time[s][c] + 1
        q.append((s-1, c))

ans = time[n][1]
for i in range(1, n+1):
    if time[n][i] != -1:
        ans = min(time[n][i], ans)

print(ans)
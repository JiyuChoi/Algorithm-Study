# 회의 수 입력
n = int(input())
# 회의 시간 입력 및 종료시간 기준으로 정렬
time = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

# 첫번째 회의가 끝나는 시간
end_time = time[0][1]
cnt = 1

for x in time[1:]:
    # 다음회의 시작이 이전회의 종료보다 늦다면 카운트
    if x[0] >= end_time:
        cnt += 1
        end_time = x[1]

print(cnt)
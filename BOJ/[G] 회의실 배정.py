import sys

n = int(input())

# 회의 시간표 입력
timetable = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

# 회의 끝나는 시간
end_time = 0
# 가능한 회의 수
cnt = 0

for s, e in timetable:
    #  다음 회의 시작시간 >= 이전 회의 끝나는 시간이면
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)
# # 회의 수 입력
# n = int(input())
# # 회의 시간 입력 및 종료시간 기준으로 정렬
# time = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
#
# # 첫번째 회의가 끝나는 시간
# end_time = time[0][1]
# cnt = 1
#
# # 시작:s, 종료:e
# for s, e in time[1:]:
#     # 다음회의 시작이 이전회의 종료보다 늦다면 카운트
#     if s >= end_time:
#         cnt += 1
#         end_time = e
#
# print(cnt)

n = int(input())
time = sorted([map(int, input().split()) for _ in range(n)], key=lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]

for s, e in time[1:]:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)
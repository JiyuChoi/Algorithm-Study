# k, n = map(int, input().split())
#
# # 보통 이렇게 함
# # line = [int(input()) for _ in range(k)]
# # max_value = max(line)
#
# line = []
# res = 0
# max_value = 0
#
# # 리스트 생성과 최댓값(e) 한 번에 처리할 수 있음
# for _ in range(k):
#     num = int(input())
#     line.append(num)
#     max_value = max(num, max_value)
#
# s = 0
# e = max_value
#
# while s <= e:
#     cnt = 0
#     mid = (s + e)//2
#     for x in line:
#         cnt += x // mid
#     if cnt < n:
#         e = mid - 1
#     else:
#         if mid > res:
#             res = mid
#         s = mid + 1
#
# print(res)

k, n = map(int, input().split())

line = []
for _ in range(k):
    line.append(int(input()))

s = 0
e = max(line)

res = 0
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for l in line:
        cnt += l//mid
    if cnt < n:
        e = mid - 1
    else:
        if mid > res:
            res = mid
        s = mid + 1

print(res)
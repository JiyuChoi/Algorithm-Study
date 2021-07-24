# n, c = map(int, input().split())
# horse = sorted([int(input()) for _ in range(n)])
# res = 0
#
# # 마구간 사이의 거리 값
# s = 1
# e = horse[-1] - horse[0]
#
# while s <= e:
#     mid = (s+e)//2
#     cnt = 1
#     des = horse[0]
#     # 마구간 사이의 거리가 mid보다 큰 경우 카운트 증가
#     for x in horse[1:]:
#         if x - des >= mid:
#             cnt += 1
#             des = x
#     if cnt < c:
#         e = mid - 1
#     else:
#         res = mid
#         s = mid + 1
#
# print(res)

# 7/23 다시!

# n = int(input())
# apple = [list(map(int, input().split())) for _ in range(n)]
# res = 0
# l = n//2
#
# # 투포인터 이용
# s = e = l
# for i in range(n):
#     for j in range(s, e+1):
#         res += apple[i][j]
#     if i < l:
#         s -= 1
#         e += 1
#     else:
#         s += 1
#         e -= 1
#
# print(res)
#
#
# # 인덱스 이용
# for i in range(n):
#     if i <= l:
#         res += sum(apple[i][l-i:l+i+1])
#     else:
#         res += sum(apple[i][i-l:l-i])
#
# print(res)


n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
res = 0
l = n//2

for i in range(n):
    if i <= l:
        res += sum(apple[i][l-i:l+i+1])
    else:
        res += sum(apple[i][i-l:l-i])

print(res)

# 투포인터 방법
s = e = l
for i in range(n):
    for j in range(s, e+1):
        res += apple[i][j]
    if i > l:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
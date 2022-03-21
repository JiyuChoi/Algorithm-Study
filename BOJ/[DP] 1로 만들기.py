# n = int(input())
# dy = [0,0,1,1]
#
# for i in range(4, n+1):
#     dy.append(dy[i-1] + 1)
#     if i % 2 == 0:
#         dy[i] = min(dy[i], dy[i//2]+1)
#     if i % 3 == 0: #elif가 아닌 if로 가야함 6의 경우 3으로 나눈 값이 더 작음
#         dy[i] = min(dy[i], dy[i//3]+1)
#
# print(dy[n])


n = int(input())
dy = [0] * 1000001

for i in range(2, n+1):
    dy[i] = dy[i-1] + 1
    if i % 3 == 0:
        dy[i] = min(dy[i//3] + 1, dy[i])
    if i % 2 == 0:
        dy[i] = min(dy[i//2] + 1, dy[i])

print(dy[n])

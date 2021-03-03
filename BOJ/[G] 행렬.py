# (0,0) (N-1,0), (0, M-1), (N-1,M-1)의 값을 결정할 수 있는 부분행렬은 딱 1개밖에 존재하지 않는다.

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
cnt = 0

# 3*3 행렬 전체를 뒤집기
def convert(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

# A, B 원소 하나씩 비교해서 같지 않으면 convert 함수 호출
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            convert(i, j)
            cnt += 1

# 전체 검사 (하나라도 일치하지 않으면 -1)
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            cnt = -1

print(cnt)
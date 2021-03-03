# 2차원 리스트 90도 회전
def rotate_90(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0]*n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠와 열쇠가 맞는지 확인
def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기를 기존의 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # 4방향으로 확인
    for _ in range(4):
        key = rotate_90(key)
        for i in range(n * 2):
            for j in range(n * 2):
                # 자물쇠에 열쇠 끼워넣기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                # 새로운 자물쇠에 열쇠가 맞는지 확인
                if check(new_lock):
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
    return False
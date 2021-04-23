import sys
n = int(sys.stdin.readline())

# 미리 최댓값까지 리스트 할당
dy = [0]*1000001
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    # 여기서 나머지 값을 넣어줘야 메모리 초과가 안남!
    dy[i] = (dy[i-1] + dy[i-2])%15746

print(dy[n])
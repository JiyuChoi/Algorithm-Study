# 성공 풀이
min_n, max_n = map(int, input().split())
ch = [1] * (max_n-min_n+1)

for i in range(2, int(max_n**0.5)+1):
    n = i**2
    # 예를 들어 min_n = 10, max_n = 20, n = 4 이면 range(8, 21, 4)이고
    # j-min_n을 계산하면 -2, 2, 6, 8 (12, 16, 18의 idx 값을 알려줌)
    # 실제 수는 min_n + n 이므로 https://peisea0830.tistory.com/34
    for j in range(min_n//n*n, max_n+1, n):
        if j-min_n >= 0 and ch[j-min_n]:
            ch[j-min_n] = 0

print(ch.count(1))


# 처음 풀이 (메모리 초과 발생)
# 접근 방법은 좋으나 효율성 X
min_n, max_n = map(int, input().split())
# num = [i for i in range(min_n, max_n+1)] # 필요 없는 부분
ch = [0] * (max_n+1)
for i in range(2, int(max_n**0.5)+1):
    n = i**2
    for j in num: # 여기서 다 보게되면 시간초과 발생 (제곱 수들만 확인)
        if j % n == 0:
            ch[j] = 1

print(ch[min_n:max_n+1].count(0))
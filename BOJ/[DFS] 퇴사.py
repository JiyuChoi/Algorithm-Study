def dfs(l, price):
    global max_v
    # 날짜가 n을 넘겼다면 종료
    if l > n:
        return
    # 날짜가 n이라면 최댓값 비교
    if l == n:
        if price > max_v:
            max_v = price

    else:
        # l일에 상담을 하는 경우
        dfs(l+T[l], price+P[l])
        # l일에 상담을 하지 않는 경우
        dfs(l+1, price)

# n값 입력
n = int(input())
T = []
P = []
# t, p 각각 T, P 리스트에 입력
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

max_v = float('-inf')

dfs(0, 0)

print(max_v)
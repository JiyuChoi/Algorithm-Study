# testcase의 개수
T = int(input())

for i in range(T):
    # 문서의 수, 확인할 문서의 인덱스
    N, M = map(int, input().split())
    # enumerate를 이용해 인덱스와 중요도를 order 리스트에 저장
    order = [[i, int(j)] for i, j in enumerate(input().split())]
    # 출력순서
    cnt = 0

    while True:
        # 가장 앞에 있는 문서의 중요도 == 가장 중요도가 높은 문서
        if order[0][1] == max(order, key=lambda x: x[1])[1]:
            cnt += 1

            # 중요도가 높은 문서의 인덱스가 찾는 것이면 순서 출력
            if order[0][0] == M:
                print(cnt)
                break

            # 찾는 것이 아니라면 인쇄한다
            else:
                order.pop(0)

        # 가장 중요도가 높은 문서가 아니라면 뒤로 빼서 넣는다
        else:
            order.append(order.pop(0))

# 9/12 풀이
from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    d = deque()
    cnt = 0

    for idx, v in enumerate(arr):
        d.append([idx, v])

    while True:
        now = d.popleft()
        if any(now[1] < x[1] for x in d):
            d.append(now)
        else:
            cnt += 1
            if now[0] == m:
                print(cnt)
                break


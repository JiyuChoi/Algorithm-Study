# 직관적이고 빠른 풀이
T = int(input())
for _ in range(T):
    n = int(input())
    scores = list(map(int, input().split()))
    results = [0]*101
    # 점수를 인덱스로 카운트
    for i in scores:
        results[i] += 1
    ans = 100
    # 100부터 0까지 확인
    for i in range(100, -1, -1):
        if results[i] > results[ans]:
            ans = i
    print(f'#{n} {ans}')


# 처음 풀이
# from collections import Counter
#
# T = int(input())
# for _ in range(T):
#     max_value = 0
#     n = int(input())
#     score = Counter(list(map(int, input().split())))
#
#     for k, v in score.items():
#         if v == score.most_common()[0][1]:
#             if k > max_value:
#                 max_value = k
#
#     print(f'#{n} {max_value}')
T = int(input())
for t in range(1, T+1):
    strs = input()
    # 1부터 10까지 패턴의 길이를 늘려가며 확인
    for n in range(1, 11):
        # 현재 문자열과 그다음 문자열이 같으면 break
        if strs[:n] == strs[n:2*n]:
            break
    print(f'#{t} {n}')


# 처음 풀었던 멍청한 풀이...
# 그냥 break 하면 되는데.. 바보
# T = int(input())
# for t in range(1, T+1):
#     strs = input()
#     cnt = 0
#     for l in range(1, 11):
#         if strs[:l] == strs[l:2*l]:
#             if 30/l > cnt:
#                 cnt = 30/l
#                 max_len = l
#     print(f'#{t} {max_len}')
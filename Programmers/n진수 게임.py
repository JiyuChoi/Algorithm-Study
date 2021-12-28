def convert(i, n):
    tmp = "0123456789ABCDEF"

    q, r = divmod(i, n) # 몫과 나머지 튜플로 주어짐

    if q == 0:
        return tmp[r]
    else:
        return convert(q, n) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    res = ''
    for x in range(t * m):
        res += convert(x, n)

    for i in range(p - 1, t * m, m):
        answer += res[i]

    return answer
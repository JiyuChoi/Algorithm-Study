def solution(s):
    answer = len(s)

    # for문 안에 answer 쓰면 안됨! 값이 계속 바뀌어서 답 이상해짐!
    for i in range(1, len(s) // 2 + 1):
        res = ""
        cur = s[:i]
        cnt = 1
        # 마지막으로 비교한 문자열 넣기: for j in range(i, len(s)+i, i)
        for j in range(i, len(s) + i, i):
            if cur == s[j:j + i]:
                cnt += 1
            else:
                if cnt != 1:
                    res += str(cnt) + cur
                else:
                    res += cur
                cur = s[j:j + i]
                cnt = 1

        if len(res) < answer:
            answer = len(res)

    return answer


'''
s = "abcabcabcabcdededededede"
print(solution(s))
'''


# 다시 푼 풀이
# 0 부터 비교한 방식 위에 풀이가 더 간결함!
s = input()
l = len(s)
answer = l

# 1개부터 압축 단위를 늘려가며 확인
for i in range(1, l // 2 + 1):
    res = ""
    cnt = 1
    for j in range(0, l, i):
        # 이전 상태와 동일하다면 압축 횟수 증가
        if s[j:j + i] == s[j + i: j + 2 * i]:
            cnt += 1
        # 더이상 압축하지 못한다면
        else:
            if cnt != 1:
                res += str(cnt) + s[j:j + i]
            else:
                res += s[j:j + i]
            cnt = 1

    # 남아 있는 문자열 처리
    # 한줄로 정리: res += str(cnt) + s[j + i: j + 2 * i] if cnt != 1 else s[j + i: j + 2 * i]
    if cnt != 1:
        res += str(cnt) + s[j + i: j + 2 * i]
    else:
        res += s[j + i: j + 2 * i]

    # 압축된 문자열 길이가 짧은 것이 정답
    if answer > len(res):
        answer = len(res)

print(answer)
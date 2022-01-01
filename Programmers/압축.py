def solution(msg):
    answer = []
    idx = [""]+[chr(n) for n in range(65, 91)]

    i = 0
    string = ""
    while i < len(msg):
        string += msg[i]
        if string in idx:
            i += 1
            continue
        else:
            answer.append(idx.index(string[:-1]))
            idx.append(string)
            string = ""

    answer.append(idx.index(string))
    return answer

msg = "KAKAO"
print(solution(msg))
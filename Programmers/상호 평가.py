def solution(scores):
    answer = ''
    for i in range(len(scores)):
        s = []
        for j in range(len(scores)):
            s.append(scores[j][i])

        if s[i] == min(s) and s.count(s[i]) == 1:
            del s[i]
        elif s[i] == max(s) and s.count(s[i]) == 1:
            del s[i]

        avg = sum(s)/len(s)

        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))

# python 이용!
# for idx, score in enumerate(list(map(list, (zip(*scores))))):
    #     if score[idx] in (max(score), min(score)) and score.count(score[idx]) == 1:
    #         del score[idx]
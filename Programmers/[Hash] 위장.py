from collections import Counter

def solution(clothes):
    answer = 1
    cnt = Counter([kind for item, kind in clothes])
    for i in cnt.values():
        answer *= (i+1) # 해당 kind에서 아무것도 안입는 경우
    return answer - 1
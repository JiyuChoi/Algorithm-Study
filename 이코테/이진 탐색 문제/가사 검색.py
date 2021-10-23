from bisect import bisect_left, bisect_right
from collections import defaultdict

def func(a, left, right):
    left_idx = bisect_left(a, left)
    right_idx = bisect_right(a, right)
    return right_idx - left_idx

def solution (words, queries):
    answer = []
    dict = defaultdict(list)
    reverse_dict = defaultdict(list)

    for word in words:
        dict[len(word)].append(word)
        reverse_dict[len(word)].append(word[::-1])

    for key in dict.keys():
        dict[key].sort()
        reverse_dict[key].sort()

    for query in queries:
        if query[0] != '?':
            answer.append(func(dict[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
        else:
            query = query[::-1]
            answer.append(func(reverse_dict[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro??", "pro?"]
solution(words, queries)

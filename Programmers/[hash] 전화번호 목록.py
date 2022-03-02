from collections import defaultdict


def solution(phone_book):
    answer = True
    hashmap = defaultdict(int)

    for pb in phone_book:
        hashmap[pb] = 1

    for phone_number in phone_book:
        temp = ""
        for pn in phone_number:
            temp += pn
            if temp in hashmap and temp != phone_number:
                answer = False

    return answer
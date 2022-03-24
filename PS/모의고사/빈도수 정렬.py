def solution(s):
    s = list(s)
    s.sort(key=lambda x: -s.count(x))
    return ''.join(s)

s = 'cccbbbaaAABB'
print(solution(s))
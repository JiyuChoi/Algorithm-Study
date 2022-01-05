from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    for city in cities:
        city = city.lower()
        if cacheSize:
            if city in cache:
                cache.remove(city)
                answer += 1
            else:
                if len(cache) == cacheSize:
                    cache.popleft()
                answer += 5
            cache.append(city)
        else:
            answer += 5

    return answer
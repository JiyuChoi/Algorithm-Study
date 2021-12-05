def solution(data):
    pattern = [data[0]]
    for i in range(1, len(data)):
        if data[i] == pattern[i % len(pattern)]:
            pattern.append(data[i])
        else:
            pattern = data[: i + 1]
    return pattern[len(data) % len(pattern) + 1]
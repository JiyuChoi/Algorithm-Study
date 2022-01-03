def solution(dirs):
    answer = 0
    d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, 1), 'R': (0, -1)}
    visited = set()
    x, y = 0, 0
    for dir in dirs:
        nx = x + d[dir][0]
        ny = y + d[dir][1]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1
        x, y = nx, ny

    return answer

print(solution("ULURRDLLU"))
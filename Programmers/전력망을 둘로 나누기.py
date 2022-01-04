def dfs(x):
    global cnt, visited
    visited.append(x)
    cnt += 1
    for y in link[x]:
        if y not in visited:
            dfs(y)

def solution(n, wires):
    global cnt, visited, link
    answer = []
    link = [[] for _ in range(n + 1)]
    for x, y in wires:
        link[x].append(y)
        link[y].append(x)

    for x, y in wires:
        visited = []
        cnt = 0
        link[x].remove(y)
        link[y].remove(x)
        dfs(1)
        answer.append(abs(n - cnt * 2)) # n-cnt, cnt 둘의 차이 abs
        link[x].append(y)
        link[y].append(x)

    return min(answer)
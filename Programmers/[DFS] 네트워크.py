# BOJ '연결 요소의 개수'와 풀이 방법 동일

def solution(n, computers):

    # dfs 함수 정의
    def dfs(i):
        # 방문 처리
        visited[i] = 1
        for j in range(n):
            # 컴퓨터끼리 연결되어있고 방문하지 않은 경우
            if computers[i][j] and not visited[j]:
                dfs(j)

    answer = 0
    visited = [0] * n

    for i in range(n):
        # 방문하지 않은 노드의 경우 새로운 네트워크로 count
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer
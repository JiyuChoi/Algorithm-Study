# 1. 백트래킹 이용
# 2. numClosed > numOpen -> invaild

def dfs(n, num_open, num_closed, string, res):
    # 종료 체크
    if num_open == n and num_closed == n:
        res.append(string)
        return
    # 재귀
    if num_open < n:
        dfs(n, num_open+1, num_closed, string+"(", res) #add open bracket
    if num_open > num_closed:
        dfs(n, num_open, num_closed+1, string+")", res) #add closed bracket

n = 3
answer = []
dfs(n, 0, 0, "", answer)
print(answer)
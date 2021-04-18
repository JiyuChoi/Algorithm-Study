def dfs(x):
    if x > 7:
        return
    else:
        # 전위 순회
        print(x, end=" ")
        dfs(2*x)
        dfs(2*x+1)
        # 중위 순회
        dfs(2*x)
        print(x, end=" ")
        dfs(2*x+1)
        # 후위 순회 (병합 정렬)
        dfs(2*x)
        dfs(2*x+1)
        print(x, end=" ")

dfs(1)
def quad_tree(x, y, n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color: # 범위안에 한개라도 다른경우는 4분면으로 나눠서 다시 검색
                answer.append("(")
                quad_tree(x, y, n//2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                answer.append(")")
                return
    answer.append(color)

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
answer = []
quad_tree(0, 0, n)
print("".join(map(str, answer)))
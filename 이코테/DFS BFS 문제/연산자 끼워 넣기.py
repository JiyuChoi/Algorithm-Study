def dfs(l):
    if l == n-1:
        res = A[0]
        for i in range(n-1):
            if ch[i] == 0:
                res += A[i+1]
            elif ch[i] == 1:
                res -= A[i+1]
            elif ch[i] == 2:
                res *= A[i+1]
            else:
                if res < 0:
                    res = abs(res)//A[i+1]
                else:
                    res //= A[i+1]
        answer.append(res)

    else:
        for i in range(4):
            if arr[i] != 0:
                ch[l] = i
                arr[i] -= 1
                dfs(l+1)
                ch[l] = 0
                arr[i] += 1



n = int(input())
A = list(map(int, input().split()))
arr = list(map(int, input().split()))
ch = [0]*(n-1)
answer = []
dfs(0)
print(max(answer))
print(min(answer))
def checkGood(ch):
    for i in range(1, n//2+1):
        if ch[-i:] == ch[-i*2:-i]:
            return False
    return True


def dfs(l):
    if l == n:
        print(*ch, sep="")
        exit() # 가장 작은값 출력하고 종료

    else:
        for i in range(1, 4):
            ch.append(str(i))
            if checkGood(ch):
                dfs(l+1)
            ch.pop()


n = int(input())
ch = ['1']
dfs(1)
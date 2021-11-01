import sys

def dfs(l):
    global max_value
    if sum(card) == n:
        res = sum([cards[x-1] for x in card if x != 0])
        if res > max_value:
            max_value = res
        return
    if l == n or sum(card) > n:
        return
    else:
        for i in range(1, n+1):
            if card[l] == 0:
                card[l] = i
                dfs(l+1)
                card[l] = 0

max_value = 0
n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
card = [0]*n
dfs(0)
print(max_value)
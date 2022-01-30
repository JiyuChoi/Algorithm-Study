# def dfs(l, tot):
#     global res
#     if l == n:
#         if 0 < tot <= sum(w):
#             res.add(tot)
#
#     else:
#         dfs(l+1, tot+w[l])
#         dfs(l+1, tot-w[l])
#         dfs(l+1, tot)
#
#
# n = int(input())
# w = list(map(int, input().split()))
# res = set()
# dfs(0, 0)
#
# print(sum(w)-len(res))

def dfs(l, tot):
    if l == n:
        if 0 < tot <= sum(w):
            res.add(tot)
        return
    else:
        dfs(l + 1, tot + w[l])
        dfs(l + 1, tot - w[l])
        dfs(l + 1, tot)

n = int(input())
w = list(map(int, input().split()))
res = set()
dfs(0, 0)

print(sum(w)-len(res))
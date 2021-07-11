# n = int(input())
# l1 = list(map(int, input().split()))
# m = int(input())
# l2 = list(map(int, input().split()))
#
# # Merge Sort: O(n) 풀이
# res = []
# i = j = 0
#
# while True:
#     if l1[i] < l2[j]:
#         res.append(l1[i])
#         i += 1
#     else:
#         res.append(l2[j])
#         j += 1
#     if i == n-1:
#         res += l2[j:]
#         break
#     if j == m-1:
#         res += l1[i:]
#         break
#
# print(*res)
#
# # O(nlogn) 풀이
# l1 += l2
# l1.sort()
# print(l1)

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

res = []
if n > m:
    n, m = m, n
    nlist, mlist = mlist, nlist

i, j = 0, 0
while i < n and j < m:
    if nlist[i] > mlist[j]:
        res.append(mlist[j])
        j += 1
    else:
        res.append(nlist[i])
        i += 1

res += mlist[j:]

print(res)
## 이진 탐색 이용한 풀이
n, m = map(int, input().split())
d_listen = [input() for _ in range(n)]
d_see = sorted([input() for _ in range(m)])
ans = []
cnt = 0

for i in d_listen:
    s = 0
    e = m - 1
    while s <= e:
        mid = (s+e)//2

        if i == d_see[mid]:
            cnt += 1
            ans.append(i)
            break

        elif i < d_see[mid]:
            e = mid - 1

        else:
            s = mid + 1

print(cnt)
for i in sorted(ans):
    print(i)




## set을 이용한 풀이
n, m = map(int, input().split())
d_listen = set([input() for _ in range(n)])
d_see = set([input() for _ in range(m)])

# 두 집합의 교집합을 이용
arr = sorted(list(d_listen & d_see))
print(len(arr))

for i in arr:
    print(i)
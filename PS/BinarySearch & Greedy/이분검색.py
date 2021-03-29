n, m = map(int, input().split())
number = sorted(list(map(int, input().split())))

# 이분탐색 => O(n)
s = 0
e = n - 1

while s <= e:
    mid = (s + e)//2
    if number[mid] == m:
        print(mid+1)
        break
    elif number[mid] < m:
        s = mid + 1
    else:
        e = mid - 1

# 선형탐색2 => O(n)
print(number.index(m)+1)

# 선형탐색
for idx, num in enumerate(number):
    if num == m:
        print(idx+1)
        break
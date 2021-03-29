n, m = map(int, input().split())
number = sorted(list(map(int, input().split())))

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

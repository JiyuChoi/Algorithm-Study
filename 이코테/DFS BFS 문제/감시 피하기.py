from itertools import combinations

n = int(input())
arr = []
teachers = []
spaces = []

for i in range(n):
    arr.append(list(input().split()))
    for j in range(n):
        if arr[i][j] == "T":
            teachers.append((i, j))
        if arr[i][j] == "X":
            spaces.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def watch(x, y, i):
    if i == 0:
        while x < n:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            x += 1
    if i == 1:
        while y < n:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            y += 1
    if i == 2:
        while x >= 0:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            x -= 1
    if i == 3:
        while y >= 0:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            y -= 1
    return False


def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        arr[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        arr[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')


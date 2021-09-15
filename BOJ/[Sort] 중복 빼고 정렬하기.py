n = int(input())
num = sorted(set(list(map(int, input().split()))))
print(*num)
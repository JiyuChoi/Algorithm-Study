n = int(input())
num = list(map(int, input().split()))

numset = list(sorted(set(num)))
numset = {numset[i] : i for i in range(len(numset))}

print(*[numset[i] for i in num])
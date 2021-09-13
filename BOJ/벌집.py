n = int(input())

num = 1

for i in range(0, n):
    if n <= num + (6*i):
        print(i+1)
        break
    num += (6*i)

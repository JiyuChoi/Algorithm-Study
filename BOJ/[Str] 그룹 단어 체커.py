n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    for w in word:
        c = word.count(w)
        if w*c not in word:
            cnt += 1
            break

print(n-cnt)
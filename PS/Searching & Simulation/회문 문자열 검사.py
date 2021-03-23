n = int(input())

# python 풀이 (코테때는 이렇게!)
for i in range(n):
    word = input().lower()
    if word == word[::-1]:
        print("%d YES" %(i+1))
    else:
        print("%d NO" %(i+1))

# 손코딩 풀이
for i in range(n):
    word = input().lower()
    for j in range(len(word)//2):
        if word[-(j+1)] != word[j]:
            print("%d NO" %(i+1))
            break
    else:
        print("%d YES" %(i+1))

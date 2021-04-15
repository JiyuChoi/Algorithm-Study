from collections import Counter
# Counter 이용 풀이
word1 = list(input())
word2 = list(input())

if Counter(word1) == Counter(word2):
    print("YES")
else:
    print("NO")

# 리스트 이용 풀이
ch_1 = [0]*52
ch_2 = [0]*52

for x in word1:
    if x.isupper():
        ch_1[ord(x) - 65] += 1
    else:
        ch_1[ord(x) - 71] += 1

for x in word2:
    if x.isupper():
        ch_2[ord(x) - 65] += 1
    else:
        ch_2[ord(x) - 71] += 1

for i in range(52):
    if ch_1[i] != ch_2[i]:
        print("NO")
        break
else:
    print("YES")
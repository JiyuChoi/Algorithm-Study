word = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# 문자열 특성을 이용한 풀이
for c in cro:
    word = word.replace(c, '*')
print(len(word))


# 처음 생각한 풀이인데 완전 노가다네
# cnt = i = 0
# while i != len(word):
#     if word[i:i+2] in cro:
#         i += 2
#     elif word[i:i+3] in cro:
#         i += 3
#     else:
#         i += 1
#     cnt += 1
# print(cnt)

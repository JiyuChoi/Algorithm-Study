# 입력된 문자열을 - 기준으로 자르기
s = input().split("-")
cnt = 0

# 첫번째 수 더하기
for i in s[0].split("+"):
    cnt += int(i)

# 두번째 수부터는 + 기준으로 나누어 빼기
for i in s[1:]:
    for j in i.split("+"):
        cnt -= int(j)

print(cnt)
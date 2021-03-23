s = input()
res = ""

for x in s:
    if x.isdecimal():
        res += x
res = int(res)
print(res)

cnt = 0
for i in range(res):
    if not res % (i+1):
        cnt += 1
print(cnt)
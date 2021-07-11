# s = input()
# res = ""
#
# for x in s:
#     if x.isdecimal():
#         res += x
# res = int(res)
# print(res)
#
# cnt = 0
# for i in range(res):
#     if not res % (i+1):
#         cnt += 1
# print(cnt)


string = input()
num = ''
for s in string:
    if s.isdigit():
        num += s
print(int(num))

cnt = 0
for i in range(1, int(num)+1):
    if int(num) % i == 0:
        cnt += 1
print(cnt)
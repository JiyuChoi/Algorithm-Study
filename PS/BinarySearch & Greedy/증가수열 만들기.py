n = int(input())
num = list(map(int, input().split()))

incre = [0]
res = ''

while True:
    tmp = incre[-1]
    left = num[0]
    right = num[-1]
    if left > tmp and right > tmp:
        if left > right:
            incre.append(num.pop())
            res += 'R'
        else:
            incre.append(num.pop(0))
            res += 'L'
    elif left > tmp and not (right > tmp):
        incre.append(num.pop(0))
        res += 'L'
    elif right > tmp and not (left > tmp):
        incre.append(num.pop())
        res += 'R'
    else:
        break

print(len(incre)-1)
print(res)
n = int(input())

five = n//5
remain = n % 5

while five >= 0:
    if remain % 3 == 0:
        print(remain // 3 + five)
        break
    five -= 1
    remain += 5

else:
    print(-1)
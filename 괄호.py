T = int(input())
for _ in range(T):
    cnt = 0
    ps = input()
    for j in ps:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
        #닫는 개수가 더 많거나 VPS가 아닌 경우
        if cnt < 0:
            print("NO")
            break
    # 여는 개수와 닫는 개수가 같은 경우
    if cnt == 0:
        print("YES")
    # 여는 개수가 더 많은 경우
    elif cnt > 0:
        print("NO")
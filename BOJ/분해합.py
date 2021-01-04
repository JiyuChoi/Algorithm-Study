n = int(input())
ans = 0

for i in range(n+1):
    m_list = list(map(int, str(i)))
    ans = i + sum(m_list)

    if ans == n:
        print(i)
        break

    if i == n:
        print(0)
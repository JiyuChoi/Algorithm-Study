a, b, v = map(int, input().split())

# 나누어 떨어지는지 구분하지 않기 위해 -1
day = (v-b-1)/(a-b)+1
print(int(day))

# 나누어 떨어지면 그대로 출력 아니면 +1
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
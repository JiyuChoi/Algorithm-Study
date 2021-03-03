# 점수 n 입력 받기
n = list(map(int, input()))
l = len(n)//2

# 반으로 나눈 왼쪽 합과 오른쪽 합이 같은 경우
if sum(n[:l]) == sum(n[l:]):
    print("LUCKY")
else:
    print("READY")
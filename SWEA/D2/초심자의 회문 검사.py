T = int(input())

for t in range(1, T+1):
    # 문자열 입력받고 오른쪽 공백 지우기
    word = input().rstrip()
    # 회문이면 1 출력
    if word == word[::-1]:
        print(f'#{t} 1')
    # 회문이 아니면 0 출력
    else:
        print(f'#{t} 0')
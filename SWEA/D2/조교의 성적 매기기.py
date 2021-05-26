T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    n, k = map(int, input().split())
    scores = []
    for i in range(1, n+1):
        mid, final, hw = map(int, input().split())
        scores.append((i, mid*0.35+final*0.45+hw*0.2)) # i==k일 때 총점을 저장해 출력시 scores.index(총점)하면 for문 한 번만 사용할 수 있dma
    scores.sort(key=lambda x: -x[1])

    for i in range(len(scores)):
        if scores[i][0] == k:
            print(f'#{t} {grade[i//(n//10)]}')
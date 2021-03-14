T = int(input())
for i in range(T):
    n, s, e, k = map(int, input().split())
    number = sorted(list(map(int, input().split()))[s-1:e])[k-1]
    print("#%d %d" %(i+1, number))

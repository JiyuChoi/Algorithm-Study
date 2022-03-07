for i in range(int(input())):
    n = int(input())
    res = ""
    if n % 2:
        res += "7"
        n -= 3
    res += "1"*(n//2)
    print(res)
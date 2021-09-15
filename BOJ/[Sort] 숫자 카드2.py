from collections import Counter
import sys

n = int(input())
card_n = Counter(list(map(int, sys.stdin.readline().split())))
m = int(input())
card_m = list(map(int, sys.stdin.readline().split()))

for i in card_m:
    print(card_n[i], end=" ")
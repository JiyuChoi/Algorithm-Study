from math import gcd
import sys

n = int(sys.stdin.readline())
trees = sorted([int(sys.stdin.readline()) for _ in range(n)])

min_l = trees[1]-trees[0]

for i in range(2, n):
    min_l = gcd(min_l, trees[i]-trees[i-1])

print((trees[-1]-trees[0])//min_l-n+1)
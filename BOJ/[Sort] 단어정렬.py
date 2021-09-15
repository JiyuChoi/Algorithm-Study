import sys

n = int(input())
word = sorted(set([sys.stdin.readline() for _ in range(n)]), key=lambda x: (len(x), x))

for w in word:
    sys.stdout.write(w)
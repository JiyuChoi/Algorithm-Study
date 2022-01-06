import re
def solution(files):
    arr = [re.split(r"([0-9]+)", file) for file in files]
    arr.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(a) for a in arr]
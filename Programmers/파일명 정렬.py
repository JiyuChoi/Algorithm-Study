import re

def solution(files):
    tmp = [re.split(r"([0-9]+)", file) for file in files]
    tmp.sort(key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(s) for s in tmp]
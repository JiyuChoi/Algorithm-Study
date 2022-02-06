import math
from collections import defaultdict

def fee_cal(fees, t):
    s_time, s_fee, e_time, e_fee = fees
    if t < s_time:
        return s_fee
    return s_fee + math.ceil((t - s_time) / e_time) * e_fee

def time_cal(out_time, in_time):
    oh, om = map(int, out_time.split(":"))
    ih, im = map(int, in_time.split(":"))
    return oh*60 + om - ih*60 - im
        
def solution(fees, records):
    answer = []
    dic2 = defaultdict(int) # 기본값 0으로!
    dic = {}
    
    for record in records:
        time, number, state = record.split()
        if state == "IN":
            dic[number] = time
            # if number not in dic2:
            #     dic2[number] = 0
        else:
            tot = time_cal(time, dic.pop(number))
            dic2[number] += tot
            
    for n, t in dic.items():
        tot = time_cal("23:59", t)
        dic2[n] += tot

    for n, t in dic2.items():
        dic2[n] = fee_cal(fees, t)
        
    for x in sorted(dic2.items(), key=lambda x: x[0]):
        answer.append(x[1])
        
    return answer

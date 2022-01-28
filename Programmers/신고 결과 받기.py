def solution(id_list, report, k):
    dic = {id: [] for id in id_list}
    mail = {id: 0 for id in id_list}

    for rp in report:
        u_id, r_id = rp.split(" ")
        if u_id not in dic[r_id]:
            dic[r_id].append(u_id)

    for v in dic.values():
        if len(v) >= k:
            for x in v:
                mail[x] += 1

    return [x for x in mail.values()]
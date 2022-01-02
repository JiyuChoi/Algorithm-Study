def change(melody):
    melody = melody.replace("C#", "c")
    melody = melody.replace("D#", "d")
    melody = melody.replace("F#", "f")
    melody = melody.replace("G#", "g")
    melody = melody.replace("A#", "a")
    return melody

def solution(m, musicinfos):
    answer = []
    m = change(m)
    for idx, info in enumerate(musicinfos):
        s, e, music, melody = info.split(",")
        shour, smin = map(int, s.split(":"))
        ehour, emin = map(int, e.split(":"))
        time = (ehour - shour) * 60 + emin - smin
        melody = change(melody)
        melody_time = (melody * time)[:time]

        if m in melody_time:
            answer.append((time, idx, music))

    if not answer:
        return "(None)"
    else:
        answer.sort(key=lambda x: (-x[0], x[1]))
        return answer[0][2]


# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
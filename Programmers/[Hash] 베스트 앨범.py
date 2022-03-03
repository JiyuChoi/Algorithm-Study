from collections import defaultdict

def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    song_info = defaultdict(list)

    for idx, genre in enumerate(genres):
        total[genre] += plays[idx]
        song_info[genre].append((idx, plays[idx]))

    total = sorted(total.items(), key=lambda x: -x[1])

    for gen in total:
        answer += sorted(song_info[gen[0]], key=lambda x: (-x[1], x[0]))[:2]

    return [x[0] for x in answer]

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42579
# hash
import time
from collections import defaultdict


def solution(genres, plays):
    answer = []
    playdict = defaultdict(list)
    genrelist = []

    # key : 장르이름, value : (횟수, 고유번호)
    for i in range(len(genres)):
        playdict[genres[i]].append((plays[i], i))

    # 장르 내에 속한 노래의 합 구하기, 우선순위에 따라 가장 많이 재생된 최대 2곡 선정
    for dict in playdict:
        genrelist.append((sum([x[0] for x in playdict[dict]]), dict))
        playdict[dict] = sorted(playdict[dict], reverse=True, key=lambda x: (x[0], -x[1]))
        playdict[dict] = playdict[dict][:2]

    # 많이 재생된 장르부터 answer 배열에 고유번호 넣기
    genrelist.sort(reverse=True)
    for genre in genrelist:
        for play in playdict[genre[1]]:
            answer.append(play[1])

    return answer


if __name__ == "__main__":
    start = time.time()  # 시작 시간 저장
    genres1 = ["classic", "pop", "classic", "classic", "pop"]
    plays1 = [500, 600, 150, 800, 2500]
    print("my ans : ", solution(genres1, plays1), " ans : [4, 1, 3, 0] time ", time.time() - start)

    genres2 = ["classic", "pop", "classic", "classic", "classic"]
    plays2 = [500, 1000, 400, 300, 200, 100]
    print("my ans : ", solution(genres2, plays2), " ans : [0, 2, 1] time ", time.time() - start)

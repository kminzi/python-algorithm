# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/43163
# bfs/dfs
import time

#방법1
def solution(begin, target, words):
    answer = 0
    if target in words:
        answer = change(begin, target, words, 0)
    return answer

#깊이 탐색이지만 전체 탐색
def change(begin, target, words, count):
    if begin == target:
        return count

    tmpWords = words.copy()
    countList = []
    for i in words:
        diff = 0 #1글자만 다른 것을 찾기 위한 변수
        for idx in range(len(begin)):
            if begin[idx] != i[idx]: diff += 1
        if diff == 1: #깊이 탐색
            tmpWords.remove(i)
            countList.append(change(i, target, tmpWords, count + 1))
    if countList:
        return min(countList)
    else:
        return count

#방문을 체크해서 동일한 탐색을 하지 않도록 수정
def solution2(begin, target, words):
    if target not in words:
        return 0
    visited = [0 for i in words]
    answer = 0
    stacks = [begin]

    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer

        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:

                if visited[i] != 0:
                    continue
                visited[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer

if __name__ == "__main__":
    start = time.time()  # 시작 시간 저장
    begin1 = "hit"
    target1 = "cog"
    words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("my ans : " + str(solution(begin1, target1, words1)) + " | ans : 4")
    print("time1 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

    start = time.time()
    begin1 = "hit"
    target1 = "cog"
    words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("my ans : " + str(solution2(begin1, target1, words1)) + " | ans : 4")
    print("time2 :", time.time() - start)

    begin2 = "hit"
    target2 = "cog"
    words2 = ["hot", "dot", "dog", "lot", "log"]
    print("my ans : " + str(solution(begin2, target2, words2)) + " | ans : 0")

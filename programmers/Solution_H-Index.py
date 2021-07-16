# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42747
# sorting

def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        index = [citation for citation in citations if citation >= answer]
        if len(index) >= answer:
            answer += 1
        else:
            return answer - 1

    index = [citation for citation in citations if citation >= answer]
    return len(index)

def solution2(citations):
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)


if __name__ == "__main__":
    citations1 = [3, 0, 6, 1, 5]
    print("my ans : " + str(solution2(citations1)) + " | ans : 3")

    citations2 = [4, 4, 4]
    print("my ans : " + str(solution2(citations2)) + " | ans : 3")

    citations3 = [22, 32]
    print("my ans : " + str(solution2(citations3)) + " | ans : 2")

    citations4 = [0, 0, 1, 1]
    print("my ans : " + str(solution2(citations4)) + " | ans : 1")

    citations5 = [6, 6, 6, 6, 6, 1]
    print("my ans : " + str(solution2(citations5)) + " | ans : 5")
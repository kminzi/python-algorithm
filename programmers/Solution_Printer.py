# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42587
# queue

def solution(priorities, location):
    answer = 0
    printDict = {} #(index, priority)형태를 가짐
    for idx, i in enumerate(priorities, 0):
        printDict[idx] = i

    printList = list(range(0, len(priorities)))

    while printList:
        tmp = printList.pop(0)
        if printDict[tmp] >= max(printDict.values()): #이번에 프린트 되는 경우
            answer += 1
            printDict.pop(tmp)
            if tmp == location: #프린트 되는 자료 = 원하는 자료
                return answer
        else: #맨 뒤로 가는 경우
            printList.append(tmp)

def solution2(priorities, location):
    answer = 0
    queue = [(idx, priority) for idx, priority in enumerate(priorities, 0)] #list로 queue구현

    while queue:
        tmp = queue.pop(0)
        if any(tmp[1] < p[1] for p in queue): #맨 뒤로 가는 경우
            queue.append(tmp)
        else: #이번에 프린트 되는 경우
            answer += 1
            if tmp[0] == location: #프린트 되는 자료 = 원하는 자료
                return answer


if __name__ == "__main__":
    priorities1 = [2, 1, 3, 2]
    location1 = 2
    print("my ans : " + str(solution(priorities1, location1)) + " | ans : 1")

    priorities2 = [1, 1, 9, 1, 1, 1]
    location2 = 0
    print("my ans : " + str(solution(priorities2, location2)) + " | ans : 5")

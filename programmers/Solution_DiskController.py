# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42627
# heap
import time
import heapq
from collections import deque

def solution(jobs):
    answer, count, currenttime = 0, 0, 0
    lasttime = -1
    jobheap = []

    while count < len(jobs):
        for job in jobs: #이전 job을 처리하는 동안 발생한 Job을 Heap에 삽입
            if lasttime < job[0] <= currenttime:
                heapq.heappush(jobheap, (job[1], job[0]))
        if jobheap:
            work, start = heapq.heappop(jobheap)
            lasttime = currenttime
            currenttime += work
            count += 1
            answer += (currenttime - start)
        else: #heap에 job이 없는 경우
            currenttime += 1

    return answer // len(jobs)


def solution2(jobs):
    #deque를 사용해서 pop 시간복잡도를 낮춤
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0

    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0: #heap에 job이 없는 경우 가장 빨리 들어올 job을 선정
            heapq.heappush(q, tasks.popleft())

    return total_response_time // len(jobs)


if __name__ == "__main__":
    start = time.time()  # 시작 시간 저장
    job1 = [[0, 3], [1, 9], [2, 6]]
    print("my ans : ", solution(job1), " | ans : 9", " time : ", time.time() - start)

    start = time.time()  # 시작 시간 저장
    job1 = [[0, 3], [1, 9], [2, 6]]
    print("my ans : ", solution2(job1), " | ans : 9", " time : ", time.time() - start)

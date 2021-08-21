#문제 링크 : https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
from collections import deque

def solution(S):
    deq = deque()
    for s in S:
        if len(deq) == 0:
            deq.appendleft(s)
            continue

        if s == '(' or s == '{' or s == '[':
            deq.appendleft(s)
        else :
            if s == ')' and deq[0] == '(':
                deq.popleft()
            elif s == '}' and deq[0] == '{':
                deq.popleft()
            elif s == ']' and deq[0] == '[':
                deq.popleft()

    if deq: return 0
    else: return 1

if __name__ == "__main__":
    S1 = "{[()()]}"
    S2 = "([)()]"
    print(solution(S1))
    print(solution(S2))
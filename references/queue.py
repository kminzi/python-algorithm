#deque(양뱡향 큐) 사용하기
#0, end index에 접근이 많은 문제에서 유용하게 사용되는 자료 구조
from collections import deque

#선언
deq = deque()

#삽입, 제거(맨 뒤, 맨 앞으로 접근 가능 O(1))
deq.append(0)
deq.appendleft(10)

deq.pop()
deq.popleft()

listExtend = [10, 22, 23]
deq.extend(listExtend)
deq.extendleft(listExtend)

#value로 삭제
deq.remove(10)

#회전
deq.rotate(1) #오른쪽으로 한 칸씩 이동, 맨 뒤 원소는 젤 앞으로 이동
deq.rotate(-1) #왼쪽으로 한 칸씩 이동, 맨 앞 원소는 젤 뒤로 이동



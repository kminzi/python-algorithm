#heapq 모듈(우선순위 큐) 사용하기
#min heap, max heap의 형태로 정렬된다. 최소/최대를 다루는 문제에서 많이 사용.

import heapq

#생성
#리스트를 힙처럼 다룰 수 있도록 하는 것이므로 list를 만들고 인자로 넘기는 방식
minheap = []

#원소 추가
heapq.heappush(minheap, 10)
heapq.heappush(minheap, 20)
heapq.heappush(minheap, 5)
print(minheap) #[5,20,10]으로 최소 힙 구성

#원소 삭제
popresult = heapq.heappop(minheap)
print(popresult) #5
print(minheap) #[10, 20]

#####
#최대 힙(기본 설정은 최소 힙 구성)
#튜플 형태로 값을 추가하면 첫번째 원소 기준으로 정렬을 하게됨
maxheap = []
heapq.heappush(maxheap, (-3,3))
heapq.heappush(maxheap, (-9,9))
heapq.heappush(maxheap, (-5,5))
print(maxheap)



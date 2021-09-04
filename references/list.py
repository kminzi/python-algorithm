#list - 자료형에 상관없이 섞어서 사용도 가능
listtest = [10, 20, 50, 30, 10, 20, 20, 20]
listrange = list(range(1,21)) #1~20 까지 리스트
print(listtest)
print(listtest.index(20)) #list 검색 후 위치 반환
#존재 여부만 확인, if n in list

listtest1 = listtest #얕은 복사, 즉 주소 값이 같아서 같이 변경됨
listtest1 = listtest.copy() #깊은 복사, 주소 값을 다르게 복사됨

listtest.append(40) #list 값 추가
listtest.insert(3, 35) #중간에 값 추가

listtest.index(10) #index위치 반환, 없으면 valueError발생
listtest.pop(0) #index 로 삭제
del(listtest[0]) #index 로 삭제
listtest.remove(20) #값을 검색하여 삭제

print(listtest.pop()) #맨 뒤에 값 제거
print(listtest.count(20)) #몇 번 나오는지 검색

listtest.sort() #정렬
listtest.reverse() #내림차순 정렬

listtest.clear() #삭제

listtest2 = ["hello", "world"]
listtest.extend(listtest2) #두개 리스트 붙이기
''.join(listtest2) #list to string
print(listtest)

import collections
c = collections.Counter(listtest)
print(c) #빈도수로 dictionary를 생성해줌

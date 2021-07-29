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



###############################
#dictionary - key/value 식으로 구성, 변수형은 무관
dicttest = {1:"hello", 2:"world", 32:"python"}
dicttest.setdefault(2, 0) #2 key 가 있으면 넘어가고 없으면 value 0 으로 세팅

from collections import defaultdict
dicttest2 = defaultdict(int) # 없는 경우 value 0으로 세팅

print(dicttest)
print(dicttest[32]) #key값으로 접근, 없으면 에러 리턴
print(dicttest.get(32)) #이렇게 접근도 가능, 없으면 default None 리턴
print(dicttest.get(3, "없으면 여기 출력"))

print(1 in dicttest) #존재 여부 판단에 따른 true/false 리턴가

dicttest[1] = "new hello" #이미 있으면 update
dicttest[3] = "new" #없으면 추가
print(dicttest)

del dicttest[3] #key delete
print(dicttest)

print(dicttest.keys()) #key print
print(dicttest.values()) #value print
print(dicttest.items()) #key-value print

dicttest.clear() #delete

###############################
#tuple - List와 같지만 변경이 안되고 대신 속도가 빠름,
menu = ("snack", "coke")
menu, price, num = "sprite", 1000, 3 #이렇게 편하게 선언이 가능해서 사용됨
print(menu[0])
print(menu, price, num)


###############################
#set - 집합, 중복이 안되고 순서가 없음
settest = {1,2,3,3,3}
print(settest) #뒤에 3은 1개만 들어감

settest2 = {2, 4, 5}
print(settest & settest2) #교집합 출력 가능
print(settest.intersection(settest2)) #같은 교집합 기능

print(settest | settest2) #합집합 출력
print(settest.union(settest2)) #같은 합집합 기능

print(settest - settest2) #차집합 출력
print(settest.difference(settest2))

settest.add(7) #추가
settest.remove(1) #삭제


#타입의 변경
testtype = {"first", "second", "third"}
print(testtype, type(testtype))

testtype = tuple(testtype)
print(testtype, type(testtype))

testtype = list(testtype)
print(testtype, type(testtype))
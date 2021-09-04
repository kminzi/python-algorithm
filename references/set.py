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
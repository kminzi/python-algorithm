# dictionary - key/value 식으로 구성, 변수형은 무관

# 선언
dicttest = {1: "hello", 2: "world", 32: "python"}
dicttest.setdefault(2, 0)  # 2 key 가 있으면 넘어가고 없으면 value 0 으로 세팅

# 초기값 설정
from collections import defaultdict

dicttest2 = defaultdict(int)  # 없는 경우 value 0으로 세팅
dicttest2 = defaultdict(list)  # 없는 경우 value []로 세팅

print(dicttest)
print(dicttest[32])  # key값으로 접근, 없으면 에러 리턴
print(dicttest.get(32))  # 이렇게 접근도 가능, 없으면 default None 리턴
print(dicttest.get(3, "없으면 여기 출력"))

print(1 in dicttest)  # 존재 여부 판단에 따른 true/false 리턴가

dicttest[1] = "new hello"  # 이미 있으면 update
dicttest[3] = "new"  # 없으면 추가
print(dicttest)

del dicttest[3]  # key delete
print(dicttest)

print(dicttest.keys())  # key print
print(dicttest.values())  # value print
print(dicttest.items())  # key-value print

dicttest.clear()  # delete

# 두 list를 합쳐서 만들기 - zip
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
score_dit = {lang: score for lang, score in zip(languages, preference)}

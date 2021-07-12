from sys import stdin
n = int(stdin.readline()) #input 보다 readline 함수를 사용하는 것이 시간 빠름
#두 차이는, input은 개행문자를 제거해주고 프롬프트 메세지를 사용한다. 하지만 sys는 개행문자를 rstrip을 통해 직접해야하고 프롬프트 메세지 불가하다.
n_list = list(map(int,stdin.readline().split()))

#기본 입출력
print("hello","hello1","hello2",sep="vs")
print("hello","hello1","hello2",end="마지막을 줄바꿈이 아닌 다른걸로 바뀜\n")

#자료구조-dictionary 출력
scores = {"math":0, "english":10, "coding":100}
for subject,score in scores.items():
    # print(subject,score)
    print(subject.ljust(8),str(score).rjust(4), sep=":") #왼쪽 정렬 8글자 / 오른쪽 정렬 4글자 확보

#남는 숫자 0으로 채우기 출력
for num in range(1, 10):
    print("0으로 번호 채우기 ", str(num).zfill(3), sep=":")

#####################################################
#랜덤 함수
from random import *
list = list(range(1,21))
shuffle(list) #리스트를 shuffle 시킴

result = sample(list, 2) #리스트에서 2개 무작위 추출
result_rand = int(random()*10)+1 #1~10 까지 랜덤
result_rand2 = randrange(5, 51) #5~50 rand

#####################################################
#문자열 슬라이싱
jumin = "990909-1129321"
print("성별 :",jumin[7]) #7번째
print("year :",jumin[0:2]) #0부터 2미만까지
print("birth :",jumin[:6]) #0부터 6미만까지
print("last :", jumin[-7:]) #-는 뒤에서 부터 숫자, 즉 뒤에 7자리부터 끝까지

#문자열 처리 함수
teststring = "Python study"
print(teststring.startswith("Python")) #시작 확인 : true
print(teststring.lower()) #소문자
print(teststring.upper()) #대문자
print(teststring[0].isupper()) #대문자인지 확인 : true
print(len(teststring)) #길이
print(teststring.replace("Python","Java")) #단어 변경

index = teststring.index("s") #문자열 위치 알려줌, 없으면 에러 발생
print(index)

print(teststring.find("n")) #같은 검색 기능, 근데 없으면 -1 리턴

print(teststring.count("n")) #해당 문자가 몇 번 나왔는지

#문자열 포맷
print("i like %d and %s" % (30,"20")) #문자면 %s, 숫자면 %d

print("i like {} and {}".format(30,20)) #중괄호를 이용한 문자열
print("i like {1} and {0}".format(30,20)) #중괄호를 이용한 문자열 - 접근응용
print("i like {age} and {age2}".format(age=20, age2=30)) #중괄호를 이용한 문자열 - 변수사용

age = 20
age2 = 30
print(f"i like {age} and {age2}") #앞에 f붙이면 바로 변수 사용 가능, 파이썬3.6부터

#탈출문자
print("hello world \nhello world2")
print('hello world "hello world" test') #작은 따옴표 사용
print("hello world \"hello world\" test") #탈출 문자 \ 사용

print("\\usr\\bin\\python3")

#문자열 리스트
liststring = ['111','112','111111','11333']
liststring.sort()
print(liststring) #길이 기준이 아니라 내부 char 비교

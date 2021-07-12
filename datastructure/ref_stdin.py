import sys

#다양한 입출력
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr) #error로 처리가능 -> 따로 로깅을 하거나 이렇게 활용

print("{0: > 10}".format(500)) #10자리 확보, 오른쪽 정렬, 빈공간은 비어있게
print("{0:_< 10}".format(500)) #10자리 확보, 왼 정렬, 빈공간은 _
print("{0: >+10}".format(500)) #10자리 확보, 오른쪽 정렬, 빈공간은 비어있게, 양수일 때 +/음수일 때-

print("{0:,}".format(1000000000)) #3자리마다 , 찍어주기

print("{0:f}".format(5/3)) #소수점 출력
print("{0:.2f}".format(5/3)) #소수점 3째 자리에서 반올림


#파일 입출력
score_file = open("test.txt", "w", encoding="utf8") #쓰기 용도(덮어쓰기), 한글때문에 utf8
print("math : 0", file=score_file, end="")
score_file.close()

score_file = open("test.txt", "a", encoding="utf8") #쓰기 용도(이어쓰기), 한글때문에 utf8
score_file.write("\nscience : 80") #따로 줄바꿈이 없기 때문에, 명시 필요
score_file.close()

score_file = open("test.txt", "r", encoding="utf8") #읽기 용도
print(score_file.read()) #전체 읽기

while True:
    line = score_file.readline() #한줄 읽고 커서는 다음 줄 로 이동
    if not line:
        break
    else:
        print(line)

lines = score_file.readlines() #list형태로 저장
print(lines)
score_file.close()

#pickle라이브러리 파일 사용
import pickle
profile_file = open("file.pickle", "wb") #binary 파일로 정의, pickle은 따로 인코딩 필요 없음
profile = {"name": "minji", "age":20, "hobby":["tennis", "computer"]}
print(profile)
pickle.dump(profile, profile_file) #profile 내용을 profile_file 에 저장
profile_file.close()

profile_file2 = open("file.pickle", "rb")
profile2 = pickle.load(profile_file2) #불러오기
print(profile2)
profile_file2.close()

#with 사용
with open("profile_file","rb") as profile_file:
    print(pickle.load(profile_file)) #with 탈출 시 알아서 close 되기에 따로 처리가 필요없음

with open("test.txt", "w", encoding="utf8") as test_file:
    test_file.write("test 입니다")
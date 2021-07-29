#기본 함수
def cal(param1, param2):
    print("cal plus={}".format(param1+param2))
    return param2

result = cal(1,3)
print(result)

#디폴트값
def profile(name, age=17, main_lang="Python"): #age를 받지 않으면 default=17
    print("name : {}\tage : {}\tmain_lang : {}".format(name,age,main_lang))

profile("test1", 60, "python")
profile("test2", main_lang="python")

#가변인자
def profile(name, age, *language):
    print("name : {}\tage : {}\t".format(name,age), end="")
    for lang in language:
        print(lang, end=" ")

profile("test3", 20, "python", "java", "c")

#지역변수, 전역변수
globaltest=10

def checkpoint(num):
    global globaltest
    globaltest -= num

checkpoint(2)
print(globaltest)
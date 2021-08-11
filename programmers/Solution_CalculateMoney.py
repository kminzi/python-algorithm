# 문제 링크 :https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = price * (sum(x for x in range(1, count+1))) - money
    if answer > 0:
        return answer
    else:
        return 0

#등차수열, max함수 이용
def solution2(price, money, count):
    answer = max(0, ((count+1)*count//2)*price-money)
    return answer

if __name__ == "__main__":
    price = 3
    money = 20
    count = 4
    print("my ans : ", solution2(price, money, count))
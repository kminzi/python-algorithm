# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42895
# dynamic Programming

# ex) N을 4번 사용한 경우는 {NNNN, (N 3번)사칙연산(N 1번), (N 2번)사칙연산(N 2번), (N 1번)사칙연산(N 3번)}으로 이루어진다.
def solution(N, number):
    answer = -1
    nList = []
    for i in range(1, 9):
        tmpSet = {int(str(N) * i)}  # {55}, {555}..
        for j in range(0, i//2):
            for k in nList[j]:
                for l in nList[i-j-2]:
                    tmpSet.add(k+l)
                    tmpSet.add(k-l)
                    tmpSet.add(l-k)
                    tmpSet.add(k*l)
                    if l != 0: tmpSet.add(k//l)
                    if k != 0: tmpSet.add(l//k)
        if number in tmpSet:
            return i
        nList.append(tmpSet)

    return answer


if __name__ == "__main__":
    N1 = 5
    number1 = 12
    print("my ans : " + str(solution(N1, number1)) + " | ans : 4")

    N2 = 2
    number2 = 11
    print("my ans : " + str(solution(N2, number2)) + " | ans : 3")

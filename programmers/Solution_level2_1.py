import math
def solution(n, a, b):
    answer = 0
    while math.ceil(a / 2) != math.ceil(b / 2):
        answer += 1
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

    return answer + 1

if __name__ == "__main__":
    n1 = 8
    a1 = 4
    b1 = 7
    print("my ans ", solution(n1, a1, b1))

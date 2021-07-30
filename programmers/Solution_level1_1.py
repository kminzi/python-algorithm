def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)

    return answer

if __name__ == "__main__":
    n1 = 123
    print("my ans ", solution(n1))

    n2 = 987
    print("my ans ", solution(n2))
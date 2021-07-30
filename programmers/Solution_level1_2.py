def solution(x):
    sumdigit = 0
    for i in str(x):
        sumdigit += int(i)
    if x % sumdigit == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = 10
    print("my ans ", solution(s1))

    s2 = 11
    print("my ans ", solution(s2))

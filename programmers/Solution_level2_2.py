import math
def solution(n, words):
    fail = 0
    for i, word in enumerate(words[1:], 1):
        if words[i - 1][-1] != word[0] or word in words[:i]:
            fail = i + 1
            break

    if fail == 0:
        return [0, 0]
    else:
        answer = [fail - n*(math.ceil(fail/n)-1) , math.ceil(fail / n)]
        return answer


if __name__ == "__main__":
    n1 = 3
    words1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "oobot", "tank"]
    print("my ans : ", solution(n1, words1))

    n2 = 2
    words2 = ["hello", "one", "dven", "never", "now", "world", "draw"]
    print("my ans : ", solution(n2, words2))


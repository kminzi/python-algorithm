# 문제 링크 : https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    binaryN = format(N, 'b') #binary로 변경
    max_count = 0
    count = 0
    for i in binaryN:
        if i == '0': #연속적인 0 카운트
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max_count

def solution2(N):
    #끝에 0을 제외하고 1로 나눈 리스트, 리스트 원소의 길이 계산
    return max([len(x) for x in format(N, 'b').strip('0').split('1')])

if __name__ == "__main__":
    num1 = 9
    num2 = 20
    num3 = 529
    num4 = 32
    print("my ans : " + str(solution(num1)) + " | ans : 2")
    print("my ans : " + str(solution(num2)) + " | ans : 1")
    print("my ans : " + str(solution2(num3)) + " | ans : 4")
    print("my ans : " + str(solution2(num4)) + " | ans : 0")

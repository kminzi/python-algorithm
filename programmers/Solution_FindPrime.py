# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42839
# 완전탐색
import itertools
import math
import time

def solution(numbers):
    answer = 0
    num_tmp = []

    #permutation 함수를 이용한 모든 순열 찾기
    for i in range(1, len(numbers) + 1):
        num_perm = list(itertools.permutations(numbers, i))
        for num in num_perm:
            num_tmp.append(int(''.join(num))) #숫자로 변환
    num_tmp = set(num_tmp) #중복 제거

    for number in num_tmp:
        if number < 2: #0,1 제외
            continue
        if isPrime(number): #소수 여부 판단
            answer += 1
    return answer

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0: return False
    return True

#에라토스테네스 체로 구현
def isPrime2(number):
    checkPrime = [True] * (number + 1)
    for i in range(2, int(math.sqrt(number)) + 1):
        if checkPrime[i]:
            j = 2
            while i * j <= number:
                if i * j == number: return False
                checkPrime[i * j] = False
                j += 1
    return True


if __name__ == "__main__":
    start = time.time()
    numbers1 = "17"
    print("my ans : ", solution(numbers1), " | ans : 3", " time : ", time.time() - start)

    start = time.time()
    numbers2 = "011"
    print("my ans : ", solution(numbers2), " | ans : 2", " time : ", time.time() - start)

    start = time.time()
    numbers3 = "2"
    print("my ans : ", solution(numbers3), " | ans : 1", " time : ", time.time() - start)

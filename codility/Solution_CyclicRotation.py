# 문제 링크 : https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

#나머지 성질을 이용한 풀이
def solution(A, K):
    result = [0]*len(A)
    for i in range(len(A)):
        result[(i+K)%len(A)] = A[i]
    return result


#K번 만큼 제일  원소 pop, 맨 앞에 insert(메모리 절약)
def solution2(A, K):
    for i in range(K):
        tmp = A.pop(-1)
        A.insert(0,tmp)
    return A

if __name__ == "__main__":
    A1 = [3, 8, 9, 7, 6]
    K1 = 3
    print("my ans : " + str(solution(A1, K1)) + " | ans : [9,7,6,3,8]")
    print("my ans : " + str(solution2(A1, K1)) + " | ans : [9,7,6,3,8]")
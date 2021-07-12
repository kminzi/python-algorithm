###순열과 조합
import itertools
import re

arr = ['a', 'b', 'c']
permutation = itertools.permutations(arr,3) #순열, N개에서 r개를 골라 순서를 고려한 나열(리턴 값의 타입이 permutation object)
p_list = list(permutation)
print(p_list) #list로 변환 필요
print(type(p_list[1])) #내부는 tuple type

combination = itertools.combinations(arr,2) #조합, n개에서 r개를 골라 순서를 고려하지 않은 조합
c_list = list(combination)
print(c_list)

#조합 재귀로 구현
def comb(list, n):
    result = []
    if n > len(list): return result
    if n == 1:
        for i in list:
            result.append([i])


###유용한 함수
z = zip([1,2,3],[4,5,6]) #iterable 객체를 묶어주는 것
print(next(z)) #(1,4) 출력

###sorting
#bubblesort
def bubblesort(test):
    for i in range(len(test)):
        for j in range(1, len(test)-i):
            if test[j-1] > test[j]:
                test[j-1], test[j] = test[j], test[j-1]
    print(test)

#selections sort, 선택정렬
def selectionsort(test):
    for i in range(len(test)):
        min_value = i
        for j in range(i+1, len(test)):
            if test[j] < test[min_value]:
                min_value = j
        test[i], test[min_value] = test[min_value], test[i]
    print(test)

def selectionsort2(test):
    for i in range(len(test)):
        min_value = min(test[i:])
        min_index = test.index(min_value)
        test[i], test[min_index] = test[min_index], test[i]
    print(test)


#cycle -> list, dict 모두 사용 가능
from itertools import cycle
listcycle = cycle([1,2,3,4,5])
for i in range(10):
    print(next(listcycle))
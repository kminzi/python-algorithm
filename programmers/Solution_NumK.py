#문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42748
#sorting

def solution(array, commands):
    answer = []
    for command in commands:
        tmpArray = array[command[0]-1:command[1]].copy()
        tmpArray.sort()
        answer.append(tmpArray[command[2]-1])
    return answer

#조금 더 간결하게
def solution2(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

if __name__ == "__main__":
    array1 =[1, 5, 2, 6, 3, 7, 4]
    command1=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print("my ans : " + str(solution2(array1, command1)) + " | ans : [5, 6, 3]")
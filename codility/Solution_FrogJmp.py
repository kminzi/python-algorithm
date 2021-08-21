#문제 링크 :https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

def solution(X, Y, D):
    length = Y - X
    if length%D == 0:
        return length//D
    else:
        return length//D + 1

if __name__ == '__main__':
    x = 10
    y = 85
    d = 30
    print(solution(x,y,d))


# https://school.programmers.co.kr/learn/courses/30/lessons/12946

# 1st try => 성공
# 재귀로 해결
def move(answer, start, other, destination, n):
    if n == 1:
        answer.append([start, destination])
        return
    if n == 2:
        answer += [start, other], [start, destination], [other, destination]
        return
    
    #가장 큰 원판 제외 모두 start -> other 이동
    move(answer, start, destination, other, n - 1)
    #가장 큰 원판 start -> destination 이동
    move(answer, start, other, destination, 1)
    #other -> destination 이동
    move(answer, other, start, destination, n - 1)
    return

def solution(n):
    answer = []
    move(answer, 1, 2, 3, n)
    
    return answer
  
  
# 2nd try (다른 사람의 풀이)
# 시간은 1st가 낫다
# yield, yield from을 알게되었다!

def solution(n):
  
    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        elif m == 2:
            yield from [[s, b], [s, d], [b, d]]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    
    return ans

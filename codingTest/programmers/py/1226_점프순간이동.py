# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    while n > 0:
        if n % 2:   # n % 2 == 1 일 때
            n = (n-1) // 2
            ans += 1
        else:
            n = n // 2
    return ans
  

# 다른 사람의 풀이
# if~else문 없앨 수 있었다!
# 다시보니 if~else문 내의 "(n-1) // 2"와 "n // 2"의 값이 같을 수밖에 없는데, 이를 합쳐준 것! 멋져멋져
def solution(n):
    ans = 0
    while n > 0:
        ans += n % 2
        n = n // 2
    return ans
  
  
# 다른 사람의 풀이_2
# 이진법 활용해서 푸는 엇-썸!한 방법이 있었다
# 그러고보니 이진수로 바꿔서 생각하면 되는거였네^^ㅎㅎㅎ
def solution(n):
    return bin(n).count('1')

# https://programmers.co.kr/learn/courses/30/lessons/12977#

# 1st try
# 중복수까지 카운팅해줘야 한다고 한다^^ 출제자가 잘못했네
from itertools import combinations

def solution(nums):
    answer = 0
    for combination in combinations(nums, 3):      
        num = sum(combination)
        for i in range(2, num//2):
            if num % i == 0:
                break
        else: answer += 1
    return answer
  
  
# 2nd try
# for문을 int(제곱근)+1 까지만 실행하도록 할 수도 있는데,
# 시간측면에서는 대부분 1st가 더 빠르다
# 아마 제곱근 구하는게 오래걸려서일듯!
from itertools import combinations

def solution(nums):
    answer = 0
    for combination in combinations(nums, 3):      
        num = sum(combination)
        for i in range(2, int(num*(0.5))+1):
            if num % i == 0:
                break
        else: answer += 1
    return answer

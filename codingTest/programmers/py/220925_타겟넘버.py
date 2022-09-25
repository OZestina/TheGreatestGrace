# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# 1st try
# 재귀를 사용해 모든 경우의 수를 구하는 방법
def check_rec(numbers, idx, target):
    count = 0
    if idx == len(numbers) - 1:
        if target == numbers[idx]:
            count += 1
        if target * -1 == numbers[idx]:
            count += 1
    else:
        count += check_rec(numbers, idx+1, target-numbers[idx])
        count += check_rec(numbers, idx+1, target+numbers[idx])
            
    return count

def solution(numbers, target):
    answer = check_rec(numbers, 0, target)
    return answer

  
# 2nd try (다른 사람의 풀이)
# 재귀를 사용하는 방법이지만 좀 더 간결하고 idx를 안쓴 버전
# 새로운 배열을 넘기는 것(더 많은 메모리를 쓸 것이니까)보다 idx를 넘기는게 더 나은 방법이라고 생각했는데 별 차이 없었다
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

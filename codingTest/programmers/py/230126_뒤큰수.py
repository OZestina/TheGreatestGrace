# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# 1st try => 시간초과
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                break
        else:
            answer.append(-1)
    
    return answer

# 2nd try => 통과
import heapq

def solution(numbers):
    answer = []
    
    sort = sorted(numbers)
    to_remove = []
    
    for i in range(len(numbers) - 1):
        while len(to_remove) and -to_remove[0] == sort[-1]:
            sort.pop()
            heapq.heappop(to_remove)
        if numbers[i] == sort[-1]:
            answer.append(-1)
            sort.pop()
            continue
        if numbers[i] == sort[-2]:
            answer.append(sort[-1])
            sort.pop(-2)
            continue
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                heapq.heappush(to_remove, -numbers[i])
                break
    answer.append(-1)
    
    return answer
  
  
  
# 3rd try (다른 사람 풀이 참고)
# 더 큰수를 바로 만나지 못한 애들만 stack으로 처리하여 진행
def solution(numbers):
    l = len(numbers)
    answer = [-1] * l
    
    stack = []
    for i in range(l - 1):
        stack.append([i, numbers[i]])
        while stack:
            if stack[-1][1] < numbers[i + 1]:
                answer[stack[-1][0]] = numbers[i + 1]
                stack.pop()
            else:
                break
    
    return answer

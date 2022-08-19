# Q1 ~ Q3

# Q1
def a_sum(number, start, n):
    count = 0
    for i in number[start:]:
        if i == n:
            count += 1
    return count


def two_sum(number, start, n):
    count = 0
    for i in range(start, len(number)-1):
        count += a_sum(number, i+1, n-number[i])
    return count


def solution(number):
    answer = 0
    for i in range(len(number)-2):
        answer += two_sum(number, i+1, -number[i])
    return answer
  
  
# Q2
# 느리다...
from collections import Counter

def solution(topping):
    answer = 0
    left = Counter(topping[:1])
    right = Counter(topping[1:])

    for i in range(len(topping)-1):
        if len(left) == len(right):
            answer += 1
        if topping[i+1] not in left:
            left[topping[i+1]] = 1
        if right[topping[i+1]] == 1:
            del right[topping[i+1]]
        else:
            right[topping[i+1]] -= 1
    return answer
  
  
# Q3
# case 1~5 통과, 실패 있음
def solution(n, roads, sources, destination):
    short_way = [-2] * (n + 1)
    short_way[destination] = 0
    queue = [destination]
    done = [destination]
    away = 1
    while len(roads) > 0 and len(queue) > 0:
        temp = roads.copy()
        check = queue.pop(0)
        for road in temp:
            if check in road:
                if road[0] == check:
                    if road[1] not in done:
                        short_way[road[1]] = away
                        queue.append(road[1])
                        done.append(road[1])
                else:
                    if road[0] not in done:
                        short_way[road[0]] = away
                        queue.append(road[0])
                        done.append(road[0])
                roads.remove(road)
        away += 1
    answer = [short_way[i] if short_way[i] != -2 else -1 for i in sources]
    return answer

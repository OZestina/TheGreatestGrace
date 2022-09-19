# https://school.programmers.co.kr/learn/courses/30/lessons/17680

# 1st try
HIT = 1
MISS = 5

def pos_cache(cities, cache, city):
    for i in range(len(cache)):
        if city.lower() == cities[cache[i]].lower():
            return i
    return -1

def solution(cacheSize, cities):
    # 캐시크기 == 0 인 경우
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    cache = []
    for i in range(len(cities)):
        incache = pos_cache(cities, cache, cities[i])
        if incache > -1:
            answer += HIT
            cache.pop(incache)
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            answer += MISS
        cache.append(i)
    
    return answer
  
  
  
# 2nd try (다른 사람의 풀이)
# 같은 방식이나 deque를 import해 캐시에 없는 경우를 더 간편하게 진행함
HIT = 1
MISS = 5

from collections import deque

def solution(cacheSize, cities):
    #create deque
    cache = deque(maxlen=cacheSize)
    
    answer = 0
    for city in cities:
        name = city.lower()
        if name in cache:
            cache.remove(name)
            answer += HIT
        else:
            answer += MISS
        cache.append(name)
    return answer

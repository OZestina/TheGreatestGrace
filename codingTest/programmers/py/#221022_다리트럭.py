# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3#
# 2nd try 내용 보고 또 보자


# 1st try
def solution(bridge_length, weight, truck_weights):
    cars = len(truck_weights)
    
    passingby = [0 for i in range(bridge_length * cars)]
    
    pos = 0
    for i in range(cars):
        while passingby[pos] + truck_weights[i] > weight:
            pos += 1
        for k in range(bridge_length):
                passingby[pos + k] += truck_weights[i]
        pos += 1
        
    return pos + bridge_length

  
  
# 2nd try (다른 사람의 풀이)
# class 정의하여 실행, 작은 테스트케이스의 경우 1st try가 더 빠르지만, 케이스가 커질 수록 2nd가 더 빠르고 메모리도 적게 사용한다
# 다음에 또 보고 공부해야지!

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count

# 이터레이터는 클래스를 반복 가능한 객체로 만듦. 모든 동작을 완료한 후 결과를 한 번에 메모리 적제
# 제너레이터는  함수를 반복 가능한 객체로 만듦. 각각의 yield를 한 번 실행시킨 후 대기상태로 들어가는 것을 반복

# ===============================================================
# Iterator
# 반복 가능한 객체가 되려면 하기 두 개의 메소드 구현해야 한다
# 1) __iter__(): 반복 가능한 객체 자신 반환 (iterate로 불렸을 때 어디에 접근해야 하는가)
# 2) __next__(): 다음 반복을 위한 값 반환 (더 이상 값이 없으면 StopIteration 예외 처리)

# range() 기능을 하는 클래스를 만들어보자
class MyCounter(object):
    def __init__(self, low, high) -> None:
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        # 값이 초과될 경우 예외처리
        if self.current > self.high:
            raise StopIteration
        else:
            # 값을 일단 +1
            self.current += 1
            # 리턴하는 것은 기존값
            return self.current - 1

c = MyCounter(1, 10)
for i in c:
    print(i)
    
# ===============================================================    
# Generators (Python 2.3 버전부터 도입)
# generators는 키워드 yield를 사용해 함수를 반복 가능한 객체로 만드는 하나의 방법
# yield 문장을 사용해 함수를 제너레이터로 만들 수 있다

def myGenerator():
    yield 'first'
    yield 'second'
    yield 'third'

for word in myGenerator():
    print(word)


def MyCounterGen(low, high):
    while low <= high:
        yield low
        low += 1

for i in MyCounterGen(1, 10):
    print(i, end=' ')


# yield from {리스트} 로 만들 수도 있다 => 리스트가 끝날때까지 대기상태로 빠지지 않는다

import time

def gen(lst):
    while True:
        yield from lst
        # 이 이후의 내용은 lst 한 바퀴가 끝난 다음에만 실행됨
        time.sleep(1)
        print(lst) 

test = gen([1,2,3,4,5])
n = next(test)
print(n)
n = next(test)
print(n)
n = next(test)
print(n)
n = next(test)
print(n)
n = next(test)
print(n)
# 더 이상 반환할 게 없으면 (gen()에 while문 없을 경우) Error (StopIteration) 발생
n = next(test)
print(n)

# generator
# yield로 함수를 처리하는 도중에 잠시 중단하고 값을 반환할 수 있다
# next 함수를 이용해 다음 값 반환 가능
# 제너레이터 겍채는 이터레이터의 일종이므로 for문을 이용해 반복처리할 수 있다

def fibonacci_generator():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1


fib_gen = fibonacci_generator()

for i in range(10):
    print(next(fib_gen))
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

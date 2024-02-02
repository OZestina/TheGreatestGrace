# closer
# 일종의 함수 객체로, 실행 시의 상태를 저장하는 영역으르 가진 것
# global 변수를 사용하지 않고, 이전에 실행한 내용을 기억해서 이용할 수 있다.

def outer_func():
    count = 0

    def inner_func():
        nonlocal count
        count += 1
        print(f'{count}번 실행됨')
    
    return inner_func

func = outer_func()
func() #1번 실행됨
func() #2번 실행됨
func() #3번 실행됨


############################################################

# decorator
# 어떤 함수에 대해 지정한 고차함수를 항상 호출한다
# 기존 함수의 코드를 변경하지 않고 추가 처리 가능

def add_msg(f):

    def func(*args, **kwargs):
        print('start')
        result = f(*args, **kwargs)
        print('end')
        return result

    return func


@add_msg
def actual_func(num):
    print('actual function')
    return num * 10


print(actual_func(5))
# start
# actual function
# end
# 50

############################################################

# closer + decorator

def counter(n):
    count = n

    def add_msg(f):
        nonlocal count

        def func(*args, **kwargs):
            nonlocal count
            count -= 1
            if count < 0:
                print('over count')
                return 0
            print('start')
            result = f(*args, **kwargs)
            print('end')
            return result

        return func
    return add_msg


@counter(3)
def actual_func(num):
    print('actual function')
    return num * 10


actual_func(5)
actual_func(5)
actual_func(5)
actual_func(5) #over count
actual_func(5) #over count

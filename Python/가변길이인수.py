# 가변 길이 위치 인수
# 인수 앞에 *를 1개 붙이면 가변 길이 위치 인수
# 함수를 호출하는 곳에서 지정한 인수가 '튜플' 형식으로 저장된다

def func(x, y, *args):
    print(f'1: {x}')
    print(f'2: {y}')
    if args:
        print(f'3, etc.: {args}')

func(1, 2, 3, 4)
# 1: 1
# 2: 2
# 3, etc.: (3, 4)



# 가변 길이 키워드 인수 (딕셔너리!)
# 인수 앞에 **를 붙이면 가변 길이 키워드 인수
# 함수를 호출하는 곳에서 지정한 인수가 '튜플' 형식으로 저장된다

def func1(x, y, **kwargs):
    print(f'x: {x}')
    print(f'y: {y}')
    if kwargs:
        print(f'3, etc.: {kwargs}')

func1(1, y=2, z=3, a=4)
# x: 1
# y: 2
# 3, etc.: {'z': 3, 'a': 4}



# 가변 길이 위치 / 키워드 인수 함께 사용
# *args, **kwargs 순서로 쓴다
def func2(x, *args, **kwargs):
    print(x)
    if args:
        print(args)
    if kwargs:
        print(f'3, etc.: {kwargs}')

func2(1, 200, 400, z=3, a=4)
# 1
# (200, 400)
# 3, etc.: {'z': 3, 'a': 4}

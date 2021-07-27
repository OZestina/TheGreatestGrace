from cgitb import reset


def add(a,b):
    return a+b

a=3
b=4
c=add(a,b)
print(c)

def say():
    return 'Hi'
a=say()
print(a)

def add2(a,b):
    print("%d, %d의 합은 %d입니다" %(a,b,a+b))
add2(2,5)

result = add(b=3, a=7)
print(result)

def add_many(*args):    #*는 매개변수를 모아서 (튜플)로 만들어준다
    result = 0
    for i in args:
        result += i
    return result

def add_many2(*a):
    result = 0
    for i in a:
        result += i
    return result

result = add_many(1,2,3)
result2 = add_many2(4,5,6)
print(result)
print(result2)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

r1 = add_mul("add", 1,2,3,4,5)
r2 = add_mul("mul", 1,2,3,4)
print(r1)
print(r2)

def print_kwargs(**kwargs): #**는 딕셔너리!
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='goo',age=3)

def add_and_mul(a,b):
    return a+b, a*b #튜플값 1개!
result = add_and_mul(3,4)
print(result)
r1, r2 = add_and_mul(3,4)
print(r1)
print(r2)

def say_myself(name, old, man=True):
    print(name)
    print(old)
    if man == True:
        print("man")
    else:
        print("not man")

a=1
def vartest(a):
    a += 1
    print(a)

vartest(a)
vartest(3)

a=1
def vartest2():
    global a    #함수 안에서 함수 밖의 변수(a)를 직접 사용하겠다
    a += 1
vartest2()
print(a)

add = lambda a,b: a+b   #lambda (매개변수1,2,3,...): (리턴값)
result = add(3,4)
print(result)

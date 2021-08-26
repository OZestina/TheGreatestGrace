#내장함수는 import가 필요 없다!
#외부 모듈은 import가 필요하다!

#abs (absolute, 절댓값 반환)
print(abs(-4))

#all: 반복 가능한 자료형을 인수로 받아 거짓이 하나라도 있으면 False 리턴
print(all([1,2,3]))
print(all([1,2,3,0]))       #False
print(all("strong baby"))
print(all([0,""]))          #False

#any: 반복 가능한 자료형을 인수로 받아 참이 하나라도 있으면 True 리턴
print(any([1,2,3,0]))       #True

#chr: ASCII 코드 값(숫자)을 받아 해당하는 문자 출력
print(chr(42))  #*
print(chr(48))  #0(zero)
print(chr(49))  #1
print(chr(65))  #A
print(chr(97))  #a

#dir: 객체가 자체적으로 가지고 있는 변수/함수 리턴
print(dir([1,2,3]))     #리스트
print(dir({1,2,3}))     #세트
print(dir({'1':'1'}))   #딕셔너리

#divmod(숫자1,숫자2): 숫자1을 숫자2로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7,3))      #(2,1) 몫이 2, 나머지가 1
#print(7//3)            #2
#print(7%3)             #1

#enumerate (열거하다): 순서가 있는 자료형(리스트,튜플,문자열)을 입력으로 받아
#인덱스 값을 포함하는 enumerate 객체를 돌려준다
for J, value in enumerate([1,2,3]): #J, value는 각각 인덱스, 값을 나타냄
    print(J,value)

#eval(expression): 실행 가능한 문자열을 입력으로 받아 그 결괏값 리턴
print(eval('1+2'))          #3
print(eval("divmod(7,3)"))  #(2,1)

#filter(함수명, 리스트): 반환값이 참인 것만 묶어서 object로 돌려준다
#                      주소값이 출력되므로, 값을 출력하려면 list 등으로 만들어서 출력한다
def positive(x):
    return x>0      #반환값이 True or False
print(list(filter(positive,[1,-3,2])))       #[1, 2]
print(list(filter(lambda x: x>0,[1,-3,2])))  #[1, 2]

#hex(x): 10진수 정수값을 입력받아 16진수(hexadecimal)로 반환
print(hex(12))  #0xc (앞의 0x는 16진수를 나타내는 표시)

#id(object): 주소값 리턴
print(id(3))    #1548610080
a = 3
print(id(a))    #1548610080

#input([prompt]): 사용자 입력을 받는 함수
#a = input("Enter>> ")
print(a)

#int(x, option) radix-10진수, 2-2진수, 16-16진수
print(int(3.6)) #3 (버림)
print(int('3')) #3 문자열->숫자 (근데 또 문자열이 소수이면 안돼...)
#print(int('11',radix)) #??? radix 없다고 나오는데 어떻게 쓰지
print(int('11',2)) #3
print(int('A',16)) #10

#isinstance(object, class) return True/False
class Person: pass
a = Person()
b = 3
print(isinstance(a,Person)) #True
print(isinstance(b,Person)) #False

#len: 입력값의 길이, 전체 개수 리턴
#print(len(3))   #TypeError: 'int' has no len
print(len("String"))    #6

#list: 반복 가능한 자료형을 리스트로 만들어줌!
print(list("python"))   #['p', 'y', 't', 'h', 'o', 'n']
a = [1,2,3]
b = a
c = list(a)             #리스트 깊은 복사
print(id(a), id(b), id(c))  #23487872 23487872 23487912

#map(함수, iterable data set): 입력받은 자료형의 각 요소를 f 수행한 값을 묶어서 돌려줌
def two_times(x): return x*2
print(list(map(two_times,[1,2,3])))

print(list(map(lambda x:x*2, [1,2,3,4])))

#max(iterable): 최댓값 리턴
print(max([1,2,3]))

#min(iterable): 최솟값 리턴
print(min([1,2,3]))

#oct(x): 10진수 정수 -> 8진수
print(oct(9))   #0o는 8진수임을 나타내주는 것

#ord(c): 문자의 ASCII코드 값 돌려주는 함수
print(ord('1')) #49

#pow(x,y): power, x의 y승 리턴
print(pow(2,3)) #8

#range([start,]stop[,step])

#round(number[,ndigits]): 반올림
print(round(4.51))  #5
print(round(4.5))   #4

#sorted(iterable) 입력값 정렬하여 리스트로 돌려줌
print(sorted([1,-5,3,-4,2-3,0,-2,-1]))  #[-5, -4, -2, -1, -1, 0, 1, 3]

#str(object): 문자열 형태로 객체를 변환하여 돌려주는 함수
print(str(3))   #'3'

#sum(iterable): 입력받은 리스트나 튜플을 합해주는 함수
print(sum([1,2,3])) #6

#tuple(iterable): 튜플형태로 바꾸어 돌려준다
print(tuple("abc"))     #('a', 'b', 'c')
print(tuple([1,2,3]))   #(1, 2, 3)
a = (1,2,3)
b = tuple(a)
print(id(a))    #35481320
print(id(b))    #35481320

#type(object): 입력값의 자료형을 알려준다
print(type(a))  #<class 'tuple'>
print(type(open("test","w")))   #<class '_io.TextIOWrapper'>

#zip(iterable*): 동일한 개수로 이루어진 자료형을 묶어준다
print(list(zip([1,2,3],[4,5,6])))   #[(1, 4), (2, 5), (3, 6)]
print(list(zip("abc",[4,5,6])))     #[('a', 4), ('b', 5), ('c', 6)]
print(list(zip("abc","def")))       #[('a', 'd'), ('b', 'e'), ('c', 'f')]

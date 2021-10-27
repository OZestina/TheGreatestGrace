#2021.10.27

#list
#리스트 생성
list01 = []             #빈 리스트
list02 = list()         #빈 리스트
list03 = list('ABC')    #['A', 'B', 'C']
list04 = list([1,2,3])  #[1, 2, 3]
list05 = list((1,2,3))  #[1, 2, 3]
list06 = list({1,2,3})  #[1, 2, 3]
list07 = list(range(5)) #[0, 1, 2, 3, 4]
list08 = list(range(3,5))   #[3, 4]
list09 = list(range(3,9,2)) #[3, 5, 7]
list10 = [None]*5       #원소값이 없는 리스트, [None, None, None, None, None]

#튜플
#immutable(원소를 변경할 수 없음)
tuple00 = ()        #()
tuple01 = tuple()   #()

tuple02 = 1,        #(1,)
tuple03 = (1,)      #(1,) #쉼표 필요!

tuple04 = 1,2,3     #(1, 2, 3)
tuple05 = 1,2,3,    #(1, 2, 3)
tuple06 = (1,2,3)   #(1, 2, 3)
tuple07 = (1,2,3, ) #(1, 2, 3)
tuple08 = 'A','B','C'   #('A', 'B', 'C')

tuple09 = tuple('ABC')  #('A', 'B', 'C')
tuple10 = tuple([1,2,3])    #(1, 2, 3)
tuple11 = tuple((1,2,3))    #(1, 2, 3)

tuple12 = tuple(range(3))   #(0, 1, 2)
tuple13 = tuple(range(2,4)) #(2, 3)
tuple14 = tuple(range(2,9,3))   #(2, 5, 8)
tuple15 = (None,) * 5       #(None, None, None, None, None)

#언팩
#변수s = 리스트/튜플
# -> 우변의 원소를 좌변의 변수에 하나씩 대입 가능
x = [1,2,3]
a,b,c = x       #좌변 변수의 개수와 우변 리스트/튜플 원소의 개수가 동일해야함!
print(b)        #2


s = [11,22,33,44,55,66,77]
print(s[0:5])           #[11, 22, 33, 44, 55]
print(s[0:7:2])         #[11, 33, 55, 77]
print(s[-2:-4])         #값을 구할 수 없는 경우 빈 배열 리턴 #[]
print(s[-4:-2])         #[44, 55]
print(s[5:8])           #[66, 77]
print(s[-3:])           #[55, 66, 77]
print(s[::2])           #[11, 33, 55, 77]
print(s[::-1])          #[77, 66, 55, 44, 33, 22, 11]
print(s[:-4])           #[11, 22, 33]
print(s[:-4:-1])        #[77, 66, 55]

x = 6
y = 2
x,y = x+2, y-4
print(x)            #8
print(y)            #-2

a = []              #빈 배열입니다.
if a:
    print('채워진 배열입니다')
else:
    print('빈 배열입니다.')

print([1,2]*2)              #[1,2,1,2]
print("36876".count("6"))   #2

#내포 표기 생성
numbers = [1,2,3,4,5]
twise = [num*2 for num in numbers if num%2==1]
print(twise)

twise2 = list(map(lambda x: 2*x, filter(lambda x: x%2==1 , numbers)))
print(twise2)

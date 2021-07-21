#id: 변수가 가리키고 있는 객체의 주소값 반환
a = [1,2,3]
print(id(a))

b = a       #얕은복사
print(b)
print(id(b))
print(a is b)   #True   #is는 가리키는 객체가 동일한지 여부 판단
k = id(a)
j = id(b)

b[1] = 4
print(a)        #[1, 4, 3]
print(b)        #[1, 4, 3]

#깊은복사 방법
#[:]
c = a[:]
a[1] = 2
print(c)        #[1, 4, 3]
print(a)        #[1, 2, 3]
print(id(c))    #id(a)와 다른 것 확인 가능

#copy모듈사용
from copy import copy
d = copy(a)
print(id(d))    #id(a)와 다른 것 확인 가능

e,f = ('Python','Life')
print(e)        #Python
print(f)        #Life
print(type(e))  #<class 'str'>
(g,h) = 'python','life'
print(g)        #python
print(h)        #life
print(type(g))  #<class 'str'>

[i,j] = ['python','life']
print(i)        #python
print(j)        #life
print(type(i))  #<class 'str'>

k = l = 'lives'

m = 4
n=5
n,m=m,n
print(m)    #5
print(n)    #4

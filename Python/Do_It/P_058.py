#문자열 포매팅
a = "I eat %d apples" % 3   # %d 정수
print(a)

a = "I eat %s apples" % "five"  # %s 문자열
print(a)

number = 3
a = "I eat %d apples, so %s left now" % (number, "five")
print(a)

#정렬
b = "%10s" % "hi"   #우측정렬
print(b)
b = "%-10sjane" % "hi"   #좌측정렬
print(b)

c = "%0.4f" % 3.141592  #소수점 표현 (반올림)
print(c)
c = "%10.4f" % 3.141592  #우측정렬+소수점 (점도 한 칸으로 카운트)
print(c)

#format 함수
d = "I eat {0} apples, so {1} left now".format(3, "five")
print(d)
d = "I eat {number} apples, so {left} left now".format(left="five", number = 3)
print(d)
d = "{0:>10}, {1:<10}, {number}, {2:=^10}".format("zero", "one", "two", number = 3)
#이름은 나중에 나와야한다 :>우측정렬 :<좌측정렬(표시없어도좌측) :^가운데정렬 #사이에 뭐 넣으면 그걸로 채워짐!
print(d)

e = "{{ 0 }}".format("zero")
print(e)

#문자열 format 앞에는 f를 붙이자
name = "홍길동"
age = 30
result = f"나의 이름은 {name}입니다. 나이는 {age}입니다"
print(result)

result2 = f"나는 내년이면 {age+1}살이 된다."
print(result2)

y = 3.141592
num1 = f'{y:=^10.4f}'
print(num1)

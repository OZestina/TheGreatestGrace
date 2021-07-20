#문자열 연산
#더하기
head = "Python"
tail = " is fun"
result = head+tail
print(result)

#곱하기
print(result*2)
print("="*50)
print("My Program")
print("="*50)

#문자열 길이 구하기
print(len(result))  #13 (띄어쓰기 포함)

#문자열 인덱싱
print(result[2])   #t (index는 0부터 시작)
print(result[-1])   #n (가장 마지막 글자)
print(result[-len(result)]) #P (가장 첫번째 글자)
a = result[2]+result[3]+result[7]+result[8] #this
print(a)

#문자열 슬라이싱
print(result[0:6])  #Python #[n:m] => n이상 m미만
print(result[5:-len(result)])   #Python #이게 되네..?


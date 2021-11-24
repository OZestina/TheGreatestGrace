#https://level.goorm.io/exam/49054/%EC%96%B4%EB%A0%A4%EC%9A%B4-%EB%AC%B8%EC%A0%9C/quiz/1

#1st try
def numSum(num):
	strNum = str(num)
	while len(strNum) > 1:
		c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0
		for i in strNum:
			if i == '1': c1 += 1
			elif i == '2': c2 += 1
			elif i == '3': c3 += 1
			elif i == '4': c4 += 1
			elif i == '5': c5 += 1
			elif i == '6': c6 += 1
			elif i == '7': c7 += 1
			elif i == '8': c8 += 1
			elif i == '9': c9 += 1
		num = 1*c1 + 2*c2 + 3*c3 + 4*c4 + 5*c5 + 6*c6 + 7*c7 + 8*c8 + 9*c9
		strNum = str(num)
	return strNum

def factorial(num):
	if num == 0:	#0일 경우
		return 1
	if num < 3:	#1,2일 경우
		return num
	if num == 3:	#3일 경우
		return 6
	result = 1
	for i in range(1, num+1):
		while i % 10 == 0:
			i = i // 10
		result *= i
		while result % 10 == 0:
			result = result // 10
	return numSum(result)

number = int(input())
print(factorial(number))


#2nd try
#숫자 카운팅을 array.count()로 하면 더 빠르려나 싶어서 해봤는데
#CPU점유율, 실행시간, 메모리 에서 크게 눈에 띄는 차이는 없었다
# => 웬만하면 쉽게 count로 해야겠다
def numSum(num):
	strNum = str(num)
	while len(strNum) > 1:
		c1 = strNum.count('1')
		c2 = strNum.count('2')
		c3 = strNum.count('3')
		c4 = strNum.count('4')
		c5 = strNum.count('5')
		c6 = strNum.count('6')
		c7 = strNum.count('7')
		c8 = strNum.count('8')
		c9 = strNum.count('9')
		num = 1*c1 + 2*c2 + 3*c3 + 4*c4 + 5*c5 + 6*c6 + 7*c7 + 8*c8 + 9*c9
		strNum = str(num)
	return strNum

def factorial(num):
	if num == 0:	#0일 경우
		return 1
	if num < 3:	#1,2일 경우
		return num
	if num == 3:	#3일 경우
		return 6
	result = 1
	for i in range(1, num+1):
		while i % 10 == 0:
			i = i // 10
		result *= i
		while result % 10 == 0:
			result = result // 10
	return numSum(result)

number = int(input())
print(factorial(number))

#https://level.goorm.io/exam/43238/%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

user_input = int(input())

result = "True"

for i in range(2,int(user_input**(1/2))+1):
	if user_input % i == 0:
		result = "False"
		break
		
print(result)



#파이썬에서 boolean값은 대문자로 시작하는 True / False 여서 boolean값으로 변수 생성 (메모리 적게 사용)

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import math
user_input = int(input())

def isPrime(n):
	if n == 1: return False
	elif n == 2: return True
	elif n % 2 == 0: return False
	for i in range(3, int(math.sqrt(n)), 2):	#int(n**(1/2))로 하면 안된다.. 연산 시간이 오려걸려서 그런걸까
		if n % i == 0: return False
	return True


print(isPrime(user_input))

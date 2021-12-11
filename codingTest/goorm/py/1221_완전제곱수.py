# https://level.goorm.io/exam/43152/%EC%99%84%EC%A0%84-%EC%A0%9C%EA%B3%B1%EC%88%98/quiz/1

import math

howMany = int(input())

def squared(howMany):
	count = 0
	for _ in range(howMany):
		num = math.sqrt(int(input()))
		if num == math.trunc(num): count += 1
	print(count)
	
squared(howMany)

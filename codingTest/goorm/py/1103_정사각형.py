#https://level.goorm.io/exam/49086/%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95%EC%9D%98-%EA%B0%9C%EC%88%98/quiz/1

#파이썬3에서는 long이 없어지고 int의 범위가 더 넓어졌다고 한다.
#64비트보다 큰 데이터도 처리할 수 있지만, 그렇다고 무한대는 아니다.


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

def sqCount(n):
	result = 0;
	for i in range(1, n+1):
		result += i*i
	return result

print(sqCount(user_input))

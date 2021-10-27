#goorm
#https://level.goorm.io/exam/43092/%EB%A6%AC%EA%B7%B8-%EA%B2%BD%EA%B8%B0-%ED%9A%9F%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
#print ("Hello Goorm! Your input is " + user_input)

def league(inputNum):
	number = int(inputNum)
	count = int(number * (number-1) / 2)
	return count

print(league(user_input))
	

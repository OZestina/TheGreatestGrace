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

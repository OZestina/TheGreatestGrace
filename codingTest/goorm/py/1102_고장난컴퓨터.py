#https://level.goorm.io/exam/49095/%EA%B3%A0%EC%9E%A5%EB%82%9C-%EC%BB%B4%ED%93%A8%ED%84%B0/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(map(lambda x: int(x), input().split(" ")))
enterTime = list(map(lambda x: int(x), input().split(" ")))

count = 1

for i in range(1, user_input[0]):
	if enterTime[i] - enterTime[i-1] > user_input[1]:
		count = 1
	else:
		count += 1
		
print(count)

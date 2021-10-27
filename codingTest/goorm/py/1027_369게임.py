#goorm
#https://level.goorm.io/exam/48757/369-%EA%B2%8C%EC%9E%84/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
#print ("Hello Goorm! Your input is " + user_input)

def count369(num):
	return len(list(filter(lambda x: x == "3" or x == "6" or x== "9", str(num))))
	
count = 0
for i in range(int(user_input)):
	count += count369(i)
	
print(count)

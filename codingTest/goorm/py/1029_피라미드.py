#goorm
#https://level.goorm.io/exam/43181/%ED%94%BC%EB%9D%BC%EB%AF%B8%EB%93%9C/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
floor = int(input())

def pyramid(floor):
	for i in range(floor):
		print(' ' * (floor-i-1), end='')
		print('*' * (2*i+1))

pyramid(floor)

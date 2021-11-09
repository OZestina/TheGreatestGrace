#https://level.goorm.io/exam/43218/%EC%8A%A4%ED%83%9D-stack/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def stack(times):
	stack = []
	for i in range(times):
		io = int(input())
		if io == 0:
			if len(stack) == 10:
				print("overflow")
			else:
				stack.append(input())
		elif io == 1:
			if len(stack) == 0:
				print("underflow")
			else:
				del stack[len(stack)-1]
		else:
			break
	for i in range(len(stack)):
		print(stack[i], end = ' ')

times = int(input())
stack(times)


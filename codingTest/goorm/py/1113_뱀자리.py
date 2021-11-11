#https://level.goorm.io/exam/51353/%EB%B1%80%EC%9D%B4-%EC%A7%80%EB%82%98%EA%B0%84-%EC%9E%90%EB%A6%AC/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def snake(arr):
	for i in range(0, n, 2):
		arr[i] = '#' * m

	for i in range(1, n, 2):
		if (i-1)%4==0:
			arr[i] = '.'*(m-1) + '#'
		else:
			arr[i] = '#' + '.'*(m-1)
	
	for i in arr:
		print(i)

[n,m] = list(map(int, input().split(" ")))
arr = list(['.' * m] * n)
snake(arr)

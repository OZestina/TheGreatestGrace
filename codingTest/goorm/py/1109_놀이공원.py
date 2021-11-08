#https://level.goorm.io/exam/88520/%EB%86%80%EC%9D%B4%EA%B3%B5%EC%9B%90/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def countMinTrash():
	[n, k] = list(map(int, input().split(" ")))
	
	area = []
	for _ in range(n):
		area.append(list(map(int, input().split(" "))))
	
	minTrash = k*k
	for i in range(n-k+1):
		for j in range(n-k+1):
			areaTrash = 0
			for l in range(i,i+k):
				for m in range(j,j+k):
					areaTrash += area[l][m]
			if areaTrash < minTrash:
				minTrash = areaTrash
				
	return minTrash

user_input = int(input())

for _ in range(user_input):
	print(countMinTrash())

#https://level.goorm.io/exam/49092/%EC%8A%A4%EB%82%98%EC%9D%B4%ED%8D%BC/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def mission(pos, snipers):
	a = []
	n1 = pos[0][0]
	for i in range(snipers):
		if n1 not in pos[i]:
			a.append(set(pos[i]))
	if len(a) == 0:
		return "YES"
	else: 
		#교집합
		inter = a[0]
		for i in range(1, len(a)):
			inter = inter.intersection(a[i])
		if len(inter) != 0:
			return "YES"
		
	a = []
	n1 = pos[0][1]
	for i in range(snipers):
		if n1 not in pos[i]:
			a.append(set(pos[i]))
	if len(a) == 0:
		return "YES"
	else: 
		#교집합
		inter = a[0]
		for i in range(1, len(a)):
			inter = inter.intersection(a[i])
		if len(inter) != 0:
			return "YES"
	return "NO"


snipers = int(input())

pos = []
for _ in range(snipers):
	pos.append([int(x) for x in input().split(" ")])
	
print(mission(pos, snipers))

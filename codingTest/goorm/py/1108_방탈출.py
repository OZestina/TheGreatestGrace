#https://level.goorm.io/exam/49105/%EB%B0%A9-%ED%83%88%EC%B6%9C%ED%95%98%EA%B8%B0/quiz/1

#배열로 했더니 검색이 너무 느려서 timeout이 뜬다
#검색이 빠른 딕셔너리로 바꿨더니 패스

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
valueArr = list(0 for i in range(int(input())))
arr = list(map(lambda x: int(x), input().split(" ")))
dic = dict(zip(arr, valueArr))
# print(dic)

user_input2 = int(input())
test = list(map(lambda x: int(x), input().split(" ")))

for i in test:
	if i in dic:
		print(1)
	else:
		print(0)

		
# 딕셔너리 대신 세트도 된다..! unordered면 검색은 다 빠른듯!

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
valueArr = list(0 for i in range(int(input())))
arr = set(map(lambda x: int(x), input().split(" ")))

user_input2 = int(input())
test = list(map(lambda x: int(x), input().split(" ")))

for i in test:
	if i in arr:
		print(1)
	else:
		print(0)

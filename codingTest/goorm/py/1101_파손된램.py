#goorm
#https://level.goorm.io/exam/49074/%ED%8C%8C%EC%86%90%EB%90%9C-%EB%9E%A8/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#입력
count = int(input())
rams = list(map(lambda x: int(x), input().split(" ")))
#2의제곱수 판별 재귀함수
def div2 (n):
	if n < 128: return False
	elif n == 128: return True
	elif n % 2 == 0: return div2(n/2)
	else: return False
#출력용 result 변수
broken = ""
brokenCount = 0
#연산
for i in range(count):
	if div2(rams[i]) == False:
		broken += str(i+1) + " "
		brokenCount += 1
#출력
print(brokenCount)
print(broken)

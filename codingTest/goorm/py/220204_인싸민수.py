# https://level.goorm.io/exam/49089/%EC%9D%B8%EC%8B%B8%EA%B0%80-%EB%90%98%EA%B3%A0-%EC%8B%B6%EC%9D%80-%EB%AF%BC%EC%88%98/quiz/1

from math import floor
[start, end] = [int(x) for x in input().split()]
if start == end:
	yaksu = start
	for i in range(2,floor(start**(1/2))):  # range(2,start//2) 로 하면 타임아웃이 뜨는 경우가 있어 제곱근(내림)으로 처리
		if start % i == 0:
			yaksu = i
			break
	print(yaksu)
else:
	print(2)

#https://level.goorm.io/exam/49084/80-%EC%B4%88%ED%8A%B9%EA%B0%80-%EC%84%B8%EC%9D%BC-%EC%9D%B4%EB%B2%A4%ED%8A%B8/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def minDistance(shops, home, loc):
	
	if shops == 2:
		return 0
	
	if shops == 3:
		minimum = -1
		for i in range(shops):
			if i == 0:
				minimum = abs(loc[i]-home)
			else:
				minimum = abs(loc[i]-home) if abs(loc[i]-home) < minimum else minimum
		return minimum
	
	minimum = -1
	for i in range(3):
		fromHome = abs(loc[i]-home) if abs(loc[i]-home) < abs(loc[i+shops-3]-home) else abs(loc[i+shops-3]-home)
		distance = loc[i+shops-3]-loc[i] + fromHome

		if i == 0:
			minimum = distance
		if minimum > distance:
			minimum = distance
	return minimum

#상점 수 및 집 위치
[shops, home] = map(int, input().split(" "))
#상점 위치 오름차순 정렬
loc = list(map(int, input().split(" ")))
loc.sort()
#함수 실행
result = minDistance(shops, home, loc)
print(result)

	

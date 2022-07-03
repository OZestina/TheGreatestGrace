# https://level.goorm.io/exam/49087/%EC%97%AC%EB%A6%84%EC%9D%98-%EB%8C%80%EC%82%BC%EA%B0%81%ED%98%95/quiz/1

#맘에 안드는 코드... 더 생각해보자

#좌표
pos = []
for i in range(3):
	pos.append([int(i) for i in input().split()])

#삼각형 여부 확인
if (pos[1][1] - pos[0][1])*(pos[2][0] - pos[0][0]) == (pos[1][0] - pos[0][0])*(pos[2][1] - pos[0][1]):
	print("0.00")
#삼각형일 경우 계산
else:
	x1 = pos[0][0]
	x2 = pos[1][0]
	x3 = pos[2][0]
	y1 = pos[0][1]
	y2 = pos[1][1]
	y3 = pos[2][1]
	x_min = min([x1, x2, x3])
	x_max = max([x1, x2, x3])
	y_min = min([y1, y2, y3])
	y_max = max([y1, y2, y3])

	area = (x_max - x_min) * (y_max - y_min)
	side_tri = [(x1-x2)*(y1-y2)*0.5, (x2-x3)*(y2-y3)*0.5, (x3-x1)*(y3-y1)*0.5]
	for i in side_tri:
		if i > 0:
			area -= i
		else:
			area += i
	#둔각삼각형일 경우 처리
	for i in pos:
		if i[0] != x_min and i[0] != x_max and i[1] != y_min and i[1] != y_max:
			x = i[0] - x_min if i[0] - x_min < x_max - i[0] else x_max - i[0]
			y = i[1] - y_min if i[1] - y_min < y_max - i[1] else y_max - i[1]
			area -= x*y
			break
	
	print(area, 0, sep='')

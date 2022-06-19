# https://level.goorm.io/exam/43059/%ED%8C%8C%EB%8F%84-%EC%84%BC%EC%84%9C/quiz/1

origin = [int(i) for i in input().split()]
sensor = []

for i in range(5):
	x, y = [int(i) for i in input().split()]
	sensor.append((x - origin[0])**2 + (y - origin[1])**2)

if min(sensor) > (origin[2])**2:
	print(-1)
else:
	for i in range(5):
		if sensor[i] == min(sensor):
			print(i+1)

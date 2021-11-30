# https://level.goorm.io/exam/60331/%EB%B9%99%EA%B8%80%EB%B9%99%EA%B8%80-1/quiz/1

howBig = int(input())
a = '  '
b = '# '

snail = [[b] * howBig]
for _ in range(howBig-1):
	snail += [[a] * howBig]

xpos = 0
ypos = howBig-1

for i in range(1, howBig):
	if i % 4 == 0:
		for _ in range(howBig - i + 1):
			ypos += 1
			snail[xpos][ypos] = b
	elif i % 4 == 1:
		for _ in range(howBig - i):
			xpos += 1
			snail[xpos][ypos] = b
	elif i % 4 == 2:
		for _ in range(howBig - i + 1):
			ypos -= 1
			snail[xpos][ypos] = b
	else:
		for _ in range(howBig - i):
			xpos -= 1
			snail[xpos][ypos] = b
			
for i in snail:
	print(*i, sep='')
